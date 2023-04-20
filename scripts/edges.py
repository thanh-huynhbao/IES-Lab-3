from cv_bridge import CvBridge, CvBridgeError 
import numpy as np
import cv2

scale = 1
delta = 0
depth = cv2.CV_16S

def process(frame):
    


    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.blur(grey, (3,3))

    edges = cv2.Canny(blur, 50,100)

    return edges

image = cv2.imread('/home/isaacnewthanh/ImgProcess/block/train/images/6dbb75eeb41b19f0fd9fcbe0ac374a4c (copy).jpeg')
o = process(image)
cv2.imshow('processed', o)
cv2.waitKey(0)