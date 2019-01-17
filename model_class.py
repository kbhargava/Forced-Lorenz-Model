#!/usr/bin/env python
################################################################################

#  Author            : Kriti Bhargava
#  Created on        : Tue Jan 15 13:02:03 EST 2019
#  Last Modified on  : Thu Sep  6 12:24:51 EDT 2018


################################################################################
"""
# An implementation of Lorenz system driven with chaotic forcing as in 

# Trpevski, I., Basnarkov, L., Smilkov, D., & Kocarev, L. (2013).
# "Empirical correction techniques: Analysis and applications to chaotically driven 
# low-order atmospheric models."
# Nonlinear Processes in Geophysics
# https://doi.org/10.5194/npg-20-199-2013

#
# dx1/dt = sigma * (y1-x1) +epsilon*z2
# dy1/dt = x1 * ( rho - z1 ) - y1
# dz1/dt = x1 * y1 - beta * z1 +delta*(x2-eta)
# dx2/dt = sigma * (y2-x2)
# dy2/dt = x2 * ( rho - z2 ) - y2
# dz2/dt = x2 * y2 - beta * z2
# The model can be integrated using the double approx. method described in L63 
# or Runge-Kutta 4 (RK4).

"""
################################################################################
import numpy as np
from params import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
class L_model:
  def __init__(self,x0,model_type,verbose=True):
    self.x   =  np.array(x0)
    self.dt  =  dt
    self.t   =  0
    self.int = True
    self.verbose    = verbose
    self.model_type = model_type
    if model_type == "true":
      self.dxdt = self._dxdt_true
    else:
      self.dxdt = self._dxdt_forced

  def advance(self,tmax=1,tw=1):
    """
    Integrate the model state by tmax timesteps
    Saving every tw timstep
    """
    x_return=np.empty((len(self.x),tmax+1))
    t_return = np.empty(tmax+1)
    for i in range(tmax):
      x_return[:,i] = self.x
      t_return[i]   =self.t
      self.rk4()
      if self.verbose:
        print self.t
        print self.x
    x_return[:,tmax] = self.x
    t_return[tmax]   =self.t
    return x_return, t_return

  def set_x(self,x0):
    self.x = x0
  
  def set_t(self,t):
    self.t = t
  
  def rk4(self):
    """
    Runge-Kutta 4-stage integration scheme
    """
    x_old = self.x
  
    k1 = self.dxdt()
    self.x = x_old +k1*self.dt/2.0
    
    k2 = self.dxdt()
    self.x = x_old+k2*self.dt/2.0
    
    k3 = self.dxdt()
    self.x = x_old+k3*self.dt
    
    k4 = self.dxdt()
    x_new = x_old + (self.dt/6)*(k1+2.0*k2+2.0*k3+k4)
    
    self.x = x_new
    self.t+=self.dt
  
  
  def _dxdt_true(self):
    """
    Calculating tendency
    """
    if self.verbose and self.int:
      self.verbose =False
      print "true model"
      time.sleep(2)
    k = np.empty_like(self.x)
    x1,y1,z1,x2,y2,z2 =self.x.T
    k[0] = sigma * (y1-x1) +eps*z2
    k[1] = x1 * ( rho - z1 ) - y1
    k[2] = x1 * y1 - beta * z1 +delta*(x2-eta)
    k[3] = sigma * (y2-x2)
    k[4] = x2 * ( rho - z2 ) - y2
    k[5] = x2 * y2 - beta * z2
    return k
  
  def _dxdt_forced(self):
    """
    Calculating tendency
    """
    alpha,gamma = get_forcing(self.model_type)
    if self.verbose and self.int:
      self.verbose =False
      print "forced model"
      print "alpha =", alpha
      print "gamma =", gamma
    k = np.empty_like(self.x)
    x1,y1,z1 =self.x.T
    k[0] = sigma * (y1-x1) + alpha
    k[1] = x1 * ( rho - z1 ) - y1
    k[2] = x1 * y1 - beta * z1 +gamma
    return k

if __name__ == '__main__':
  #x0 = [0.0,1.0,0.0,0.0,1.0,0.0]
  x0 = np.load("IC_true_attr.npy")[0:3]
  print x0
  timesteps = 1000000
  model = L_model(x0,"set_forcing",True)
  x,t = model.advance(tmax=timesteps)
  np.save("test_run",x)
