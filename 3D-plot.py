import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv
radius=1
Vz=1
t=np.linspace(0,10,1000,endpoint=False)
x=radius*np.cos(2*np.pi*t)
y=radius*np.sin(2*np.pi*t)
z=Vz*t
fig=plt.figure()
sub=fig.add_subplot(111,projection="3d")
sub.set_title("subplot",fontsize=12)
fig.suptitle("3D plot",fontsize=12)

sub.set_xticks([-1,-0.5,0,0.5,1])
sub.set_yticks([-1,-0.5,0,0.5,1])
sub.set_zticks([0,2,4,6,8,10])

sub.set_xlabel("$x$",fontsize=15)
sub.set_ylabel("$y$",fontsize=15)
sub.set_zlabel("$z$",fontsize=15)
sub.plot(x,y,z,linewidth=2,color="C1",label="line")
sub.legend(loc="lower left")
plt.show()
