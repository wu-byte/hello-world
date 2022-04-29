import numpy as np
import cv2
import matplotlib.pyplot as plt
img=plt.imread("1.jpg")
img=img[:,:,0]
sc=plt.imshow(img)
sc.set_cmap('jet')
sc.set_clim(0,500)
plt.colorbar()
plt.show()