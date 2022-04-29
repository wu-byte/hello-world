import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
imgL=cv.imread("view1.png",0)
imgR=cv.imread("view6.png",0)
stereo=cv.StereoSGBM_create(minDisparity=0,numDisparities=144,blockSize=31)
stereo_Gc=cv.StereoGc
#stereo=cv.StereoBM_create(numDisparities=160,blockSize=21)
disparity=stereo.compute(imgL,imgR)
wls = cv.ximgproc_DisparityWLSFilter(stereo)
filtered_disparity_map = wls.filter(disparity, imgL)
cv.stereoRectify()
#plt.imshow(disparity)
#img=cv.applyColorMap(disparity,cv.COLORMAP_HOT)
plt.imshow(filtered_disparity_map)
plt.show()
#cv.imshow("img",img)
#cv.waitKey(0)