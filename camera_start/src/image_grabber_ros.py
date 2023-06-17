import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

import TIS


class TisCameraRos():

    def __init__(self):
        self.camera = TIS.TIS()
        # the camera with serial number 10710286 uses a 640x480 video format at 30 fps and the image is converted to
        # RGBx, which is similar to RGB32.
        self.camera.open_device("05320037", 640, 480, "30/1", TIS.SinkFormats.BGRA, True)
        # Just in case trigger mode is enabled, disable it.
        self.camera.set_property("TriggerMode", "Off")

    def set_properties(self):
        print("Value of ExposureAuto before is " + str(self.camera.get_property("ExposureAuto")))
        print("Value of ExposureTime before is " + str(self.camera.get_property("ExposureTime")))
        self.camera.set_property("ExposureAuto", "Off")
        self.camera.set_property("ExposureTime", 4000)
        print("Value of ExposureAuto after is " + str(self.camera.get_property("ExposureAuto")))
        print("Value of ExposureTime after is " + str(self.camera.get_property("ExposureTime")))

    def publish_images(self):
        self.camera.start_pipeline()
        bridge = CvBridge()
        pub = rospy.Publisher('/webcam', Image, queue_size=1)
        rospy.init_node('image', anonymous=False)
        while True:
            try:
                if self.camera.snap_image(5):
                    image = self.camera.get_image()  # ITS NUMPY IMAGE
                    msg = bridge.cv2_to_imgmsg(image, "rgba8")
                    pub.publish(msg)
            except (CvBridgeError, AttributeError) as error:
                print("Some issues with tiscamera.Stopping publisher. Cause " + str(error))
                self.camera.stop_pipeline()
                break
        self.camera.stop_pipeline()
        print('Publishing ends')



if __name__ == "__main__":
    tis_camera = TisCameraRos()
    tis_camera.set_properties()
    tis_camera.publish_images()
