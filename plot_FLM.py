#!/usr/bin/env python
################################################################################

#  Author            : Kriti Bhargava

#  Created on        : Thu Jan 17 13:49:33 EST 2019
#  Last Modified on  : Thu Sep  6 12:24:51 EDT 2018


################################################################################
"""
This code contains all the subroutines to plot for the chaoticaaly driven 
low-order atmospheric model empirical online correction
"""
################################################################################
import numpy as np
from params import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def plot3d(ax,x,y,z,label_list, lims_dict,title):  
  ax.plot(x,y,z,linewidth=0.25)
  ax.set_title(title)
  ax.set_xlabel(label_list[0])
  ax.set_ylabel(label_list[1])
  ax.set_zlabel(label_list[2])
  ax.set_xlim(lims_dict["x"])
  ax.set_ylim(lims_dict["y"])
  ax.set_zlim(lims_dict["z"])

def plot2d(ax,x,y,label,xlabel="none",ylabel="none",title="none",lstyle='-',color='b',xlim=[],ylim=[]):  
  ax.plot(x,y,label=label,linestyle=lstyle,color=color)
  if not title == "none":
    ax.set_title(title)
  if not xlabel == "none":
    ax.set_xlabel(xlabel)
  if not ylabel == "none":
    ax.set_ylabel(ylabel)
  if xlim:
    ax.set_xlim(xlim)
  if ylim:
    ax.set_ylim(ylim)
  ax.legend()
