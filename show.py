import numpy as np
import cv2
img=cv2.imread("Figure_1.png",0)
img_color=cv2.applyColorMap(img,cv2.COLORMAP_COOL)
cv2.imshow("img_color",img_color)
cv2.waitKey(0)
