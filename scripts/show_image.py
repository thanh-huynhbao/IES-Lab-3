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
class show_image:
    
    def __init__(self):
        # self.name = name 
        # self.image_pub = rospy.Publisher("/image_topic_2",Image)
        # rospy.init_node(self.name)
        # self.cv_window_name = self.name
        # cv2.namedWindow(self.cv_window_name,cv2.WINDOW_NORMAL)
        # cv2.moveWindow(self.cv_window_name, 25, 75)

        self.br = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.callback, queue_size=1)

        # rospy.loginfo('Waiting ...')
        # rospy.spin()

    def callback(self, ros_image):
        try:
            img = self.br.imgmsg_to_cv2(ros_image, 'bgr8')
        except CvBridgeError as e:
            print(e)

        # frame1 = np.array(img, dtype=np.uint8)
        # cv2.imshow(self.name, frame1)

        (rows, cols, channels) = img.shape
        if cols >60 and rows >60:
            cv2.circle(img, (50,50), 10, 255)

        cv2.imshow('image window', img)
        cv2.waitKey(3)

        # try:
        #     self.image_sub.publish(self.br.cv2_to_compressed_imgmsg(img, 'bgr8'))
        # except CvBridgeError as e:
        #     print(e)
    #     self.keystroke = cv2.waitKey(5)
    #     if self.keystroke != -1:
    #         cc = chr(self.keystroke & 255).lower()
    #         if cc == 'q':
    #             rospy.signal_shutdown('Press q to quit! ')

    # def cleanup(self):
    #     print('clean')
    #     cv2.destroyAllWindows()

def main(args):
    ic = show_image()
    rospy.init_node('chow_chow', anonymous=True)
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