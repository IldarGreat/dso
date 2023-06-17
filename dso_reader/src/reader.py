#!/usr/bin/env python3
import multiprocessing
import os

import cv2
import numpy
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
# import serial
from std_msgs.msg import String

bridge = CvBridge()


###
class ReaderRos():

    def __init__(self):
        # Propeties for uart connection to copter
        print("Opening port ttyUSB0")
        # self.ser = serial.Serial("/dev/ttyUSB0")
        print("Setting baudrate 9600")
        # self.ser.baudrate = 9600
        ###
        # Propeties dso
        self.calib = '/home/pavel/app/catkin_ws/src/dso/camera.txt'
        self.mode = '1'
        self.preset = '0'
        ###

    def listener(self):
        print("Initialazing listener node")
        rospy.init_node('listener', anonymous=True)
        print("Subscribing to cam_pub node")
        rospy.Subscriber("cam_pub", String, self.dso_callback)
        print("Subscribing to webcam node")
        rospy.Subscriber("webcam", Image, self.image_callback)
        rospy.spin()

    # Info from dso
    def dso_callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "We heard %s", data.data)
        with open("result_reader.txt", "a") as myfile:
            myfile.write(data.data)
        # To write info to copter use: ser.write(b'$2,some data#')

    # Coming images from camera
    def image_callback(self, img_msg):
        try:
            cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            # cv2.imshow("Image Window", cv_image)
            avg_color_per_row = numpy.average(cv_image, axis=0)
            avg_color = numpy.average(avg_color_per_row, axis=0)
            print("Image average color = ", avg_color)
        except CvBridgeError:
            rospy.logerr("CvBridge Error: {0}")

    def launch_dso(self):
        process = multiprocessing.Process(target=self.start_dso)
        process.start()

    def start_dso(self):
        # os.system("rosrun dso_ros dso_live image:=/webcam calib=" + self.calib + " mode=" + self.mode + " preset=" + self.preset + " sampleoutput=1 nogui=1 nolog=1 quiet=1")
        # os.system("rosrun dso dso_usuall files=/home/pavel/Work/nano/dso/08.05.23/sequence calib=/home/pavel/Work/nano/dso/08.05.23/camera.txt mode=1 preset=0 sampleoutput=1 nogui=1 nolog=1 quiet=1")
        os.system("rosrun dso_fic sender.py")

    def kill_dso(self):
        # os.system("rosnode kill dso_live")
        os.system("rosnode kill dso_usuall")


###

if __name__ == "__main__":
    reader = ReaderRos()
    reader.listener()
