#!/usr/bin/env python

"""
    A ROS node that reads depth data from a RealSense camera and displays
    the distance from the camera to the object seen in the centre pixel
    of the image.
    demonstates how to use depth images & RealSense Camera

    Prior to launching this code, need to launch:
    roslaunch realsense2_camera rs_camera.launch

    Source: Brendan Halloran
"""

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

# Constants
DEPTH_SCALE = 0.001     # Depth is given in integer values on 1mm

class StreamImage(object):

    def __init__(self):

        self.image_sub = rospy.Subscriber("/camera/depth/image_rect_raw",Image,self.camera_callback)
        self.bridge_object = CvBridge()

    def camera_callback(self,data):
        try:
            cv_image = self.bridge_object.imgmsg_to_cv2(data,desired_encoding="passthrough")
        except CvBridgeError as e:
            print(e)
        
        #load image values into an array
        depth_array = np.array(cv_image, dtype=np.float32)

        #get info about shape of captured image
        height, width = cv_image.shape
        #find center pixel
        cx = width/2
        cy = height/2

        #Draw circle on image to indicate detected centroid
        cv2.circle(cv_image, (int(cx), int(cy)), 5,(0,0,0), -1)
        
        #print the distance at centre pixel to screen
        print "center depth: {0}".format( DEPTH_SCALE * depth_array[cy, cx])

        #show image on screen. Refresh every 1mS
        cv2.imshow('Depth Image',cv_image)
        cv2.waitKey(1)

def main():
    stream_image_object = StreamImage()
    rospy.init_node('stream_depth_image', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    