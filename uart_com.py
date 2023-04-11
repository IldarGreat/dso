#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial

ser = serial.Serial("/dev/ttyS0", 9600)

def callback(data):
    ser.write(data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/cam_pub", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
