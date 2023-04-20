from cv_bridge import CvBridge, CvBridgeError 
import numpy as np
import cv2


def process(frame):
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5),np.float32)/25
    im_fil = cv2.filter2D(grey,-1,kernel)
    ret, thresh = cv2.threshold(im_fil, 30,255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0),3)
    cnt = contours[0]
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(frame, (cX,cY),7,(0,0,255),-1)
    return frame


    

image = cv2.imread('/home/isaacnewthanh/ImgProcess/block/train/images/6dbb75eeb41b19f0fd9fcbe0ac374a4c (copy).jpeg')
o = process(image)
cv2.imshow('processed', o)
cv2.waitKey(0)