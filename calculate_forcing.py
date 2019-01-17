#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from params import *
"""

This code calculates the average chaotic forcing in
the 10^6 timestep nature run
"""
x_truth=np.load("truth.npy")
F1 = eps*x_truth[5,:]
F2= delta*(x_truth[3,:]+eta)

fig=plt.figure(figsize=(7,3))
ax=fig.add_subplot(111)
t=np.linspace(0,10000,1000001)
ax.plot(t,F1,label="F1 Mean forcing=%f" %np.mean(F1),linewidth=0.25)
ax.plot(t,F2,label="F2 Mean forcing=%f" %np.mean(F2),linewidth=0.25)
ax.set_xlabel("Time in MTUs")
ax.set_ylabel("Chaotic forcing")
ax.set_title(("Chaotic forcing of true system\n F1 is the forcing in x1 and F2 is forcing in z1"))
ax.legend(prop={"size":10})
plt.subplots_adjust(0.1,0.2,0.9,0.8)
fig.savefig("Mean_forcings.png",dpi=300) 
plt.show()
