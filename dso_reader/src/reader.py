#!/usr/bin/env python
import rospy
#import serial
from std_msgs.msg import String


def callback(data):
    # data.data - Строка приходящая из DSO
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # ser.write - отправка информации полетному блоку по юарту
    #ser.write(b'$2,some data#')


def listener():
    print("Listen!")
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("cam_pub", String, callback)
    # Ждем из топика cam_pub строки высылаемые из dso, каждый раз вызыватеся функция callback
    rospy.spin()


if __name__ == "__main__":
    print("Starting reading dso result in real time")
    print("Opening port ttyUSB0")
    #ser = serial.Serial("/dev/ttyUSB0")
    print("Setting baudrate 9600")
    #ser.baudrate = 9600
    listener()

