from cv_bridge import CvBridge, CvBridgeError 
import numpy as np
import cv2

scale = 1
delta = 0
depth = cv2.CV_16S

def process(frame):
    


    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    g_x = cv2.Sobel(grey, depth, 1,0,ksize = 3, scale = scale, delta = delta, borderType=cv2.BORDER_DEFAULT)
    g_y = cv2.Sobel(grey, depth, 0,1,ksize = 3, scale = scale, delta = delta, borderType=cv2.BORDER_DEFAULT)

    abs_grad_x = cv2.convertScaleAbs(g_x)
    abs_grad_y = cv2.convertScaleAbs(g_y)

    sobel = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)
    return sobel

image = cv2.imread('/home/isaacnewthanh/ImgProcess/block/train/images/6dbb75eeb41b19f0fd9fcbe0ac374a4c (copy).jpeg')
o = process(image)
cv2.imshow('processed', o)
cv2.waitKey(0)