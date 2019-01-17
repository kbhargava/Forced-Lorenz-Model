#!/usr/bin/env python
# described model parameters
import numpy as np
import random
sigma = 10.0
rho   = 28.0
beta  = 8./3
eps   = 1.0
delta = 1.0
eta   = 2.0
dt    = 0.01

pos_filename="pos_list.npy"
# forced model forcings
def get_forcing(f_type):
  if f_type == "set_forcing":
    alpha = 30.0
    gamma = 4.0
    return alpha,gamma
  elif f_type == "clim_forcing":
    alpha = 23.5
    gamma = 2.0
    return alpha,gamma
  else:
    print "f_type not specified.\n Choose f_type from (set_forcing, clim_forcing)"

# chosing random point
def random_pos(low_lim,up_lim, num_pts,save=False):
  print "up_lim=", up_lim, int(up_lim)
  print "num=", num_pts
  my_randoms = np.array(random.sample(xrange(int(up_lim)), num_pts))+low_lim
  print np.shape(my_randoms)
  if save:
    np.save(pos_filename,my_randoms)

def get_pos_list():
  pos_list = np.load(pos_filename)
  return pos_list
