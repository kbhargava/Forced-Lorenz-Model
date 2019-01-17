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
from  model_class import *
from plot_FLM import *

x0 = np.load("IC_true_attr.npy")[0:3]
print x0
timesteps = 1000000
model_type="clim_forcing"
model = L_model(x0,model_type,True)
x,t = model.advance(tmax=timesteps)
print ("Printing x now")
print (x[:,-1])
#np.save("IC_true_attr",x[:,-1])
np.save("free_climF_pIC",x)
x1=x[0,:]
y1=x[1,:]
z1=x[2,:]
if model_type=="true":
  x2=x[3,:]
  y2=x[4,:]
  z2=x[5,:]
else:
  x_truth = np.load("truth.npy")
  x2=x_truth[0,:]
  y2=x_truth[1,:]
  z2=x_truth[2,:]
"""
PLotting figure now
"""

fig = plt.figure(figsize=(8,4))
label_list=["X1", "Y1", "Z1" ,"X2","Y2","Z2"]
lims_dict={"x":(-30,30),"y":(-25,25),"z": (0,50)}

ax = fig.add_subplot(221,projection='3d')
plot3d(ax,x1,y1,z1,label_list,lims_dict, "X1 Y1 Z1 from \n Constant forcing Lorenz model\n alpha=23.5 and gamma=2") 

ax = fig.add_subplot(222,projection='3d')
plot3d(ax,x2,y2,z2,label_list[0:3],lims_dict, "X1 Y1 Z1 from \n Chaotically forced Lorenz model\n")


t=np.linspace(0,10000,1000001)

ax = fig.add_subplot(614)
label="X1 diff \n %.2f" %np.mean(x1-x2)
print label
plot2d(ax,t,x1-x2,label="X1 diff \n %.2f" %np.mean(x1-x2)
,xlim=(0,10001),color='r')

ax = fig.add_subplot(615)
label="Y1 diff \n %.2f" %np.mean(y1-y2)
plot2d(ax,t,y1-y2,label,xlim=(0,10001),color='b')

ax = fig.add_subplot(616)
label="Z1 diff \n %.2f" %np.mean(z1-z2)
plot2d(ax,t,y1-y2,label,xlim=(0,10001),color='b',xlabel="Time in Model time Units MTUs")

fig.savefig("Truth_climF_pIC.png",dpi=300)
plt.show()

plt.close()

fig =plt.figure(figsize=(7,3))
L2norm= (x1-x2)*2 + (y1-y2)*2 +(z1-z2)*2
print np.shape(L2norm)
ax=fig.add_subplot(111)
plot2d(ax,t,L2norm, label="L2norm for constant forcing Lorenz model", xlabel="Time in model time units (MTU)")
fig.savefig("L2norm_climF_pIC.png",dpi=300)
plt.show()

