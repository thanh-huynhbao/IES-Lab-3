#!/usr/bin/env python
from __future__ import print_function

import roslib
# roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
class show_image:
    
    def __init__(self):
        

        self.br = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.callback, queue_size=1)

        

    def callback(self, ros_image):
        try:
            img = self.br.imgmsg_to_cv2(ros_image, 'bgr8')
        except CvBridgeError as e:
            print(e)

        

        (rows, cols, channels) = img.shape
        if cols >60 and rows >60:
            cv2.circle(img, (50,50), 10, 255)
        display = self.process(img)
        cv2.imshow('image window', display)
        cv2.waitKey(3)

    def process(self, img):
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((5,5),np.float32)/55
        gauss = cv2.filter2D(grey,-1,kernel)
        # gauss = cv2.GaussianBlur(grey, (5,5),0)
        return gauss 
        

def main(args):
    ic = show_image()
    rospy.init_node('chow_filter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('down')
    cv2.destroyAllWindows

if __name__ == '__main__':
    # try:
    #     name = 'show_img'
    #     cam = show_image(name)
    # except KeyboardInterrupt:
    #     print('Shutting down')
    #     cv2.destroyAllWindows()
    main(sys.argv)