# ROS Wrapper around DSO: Direct Sparse Odometry

For more information see
[https://vision.in.tum.de/dso](https://vision.in.tum.de/dso)

This is meant as simple, minimal example of how to integrate DSO from a different project, and run it on real-time input data.
It does not provide a full ROS interface (no reconfigure / pointcloud output / pose output).
To access computed information in real-time, I recommend to implement your own Output3DWrapper; see the DSO code.


### Related Papers

* **Direct Sparse Odometry**, *J. Engel, V. Koltun, D. Cremers*, In arXiv:1607.02565, 2016

* **A Photometrically Calibrated Benchmark For Monocular Visual Odometry**, *J. Engel, V. Usenko, D. Cremers*, In arXiv:1607.02555, 2016


### About ROS
ROS (Robot Operating System) is a set of tools designed to develop software components in the field of robotics.
# 0. Docker
## See https://github.com/IldarGreat/dso/blob/ros_catkin/docker/README.md to run ros dso in docker!
# 1. Installation

## 1. Install DSO. <br>
We need DSO to be compiled with OpenCV (to read the vignette image), and with Pangolin (for 3D visualization). See the branch master
## 2. Install ROS <br>
ROS has several versions currently supported, melodic version on Ubuntu 18.04, noetic version on Ubuntu 20.4 (if you have Ubuntu 16.04 there is kinetic for it - no longer supported). <br>

To install ROS, select the version you need and go to the official Installation/Ubuntu - ROS Wiki documentation (https://wiki.ros.org/Installation/Ubuntu). Follow the documentation in paragraph 1.2,1.3,1.4, 1.5 (there is only the second pair of commands to set the path to ROS)

Please note that you must have at least 2 GB of free space to install ROS.

Check if the ros was installed with the command: <code>dpkg -s ros-(distro version)-ros</code>
## 3. Install catkin
For build, instead of a cmake, katkin is used. Install it <code>sudo apt-get install ros-(distro version)-catkin</code> <br>
Please learn how to use katkin, for example packages and workspace
## 4. Install package usb_cam
usb_cam is the ros package that allows you to use images from a usb camera to ros nodes <br>
Install it <code>sudo apt install ros-(distro version)-usb-cam</code> <br>
Configure usb_cam for you camera before use it. Change file /opt/ros/(distro version)/share/usb_cam/launch/usb_cam-test.launch
## 5. Export dso package
<code>export dso (path)</code>
Or you can change CMakeList.txt and specify the path to dso in it
# 3 Usage
## 1. Run ros core
<code>roscore</code> <br>
Do not close the terminal in which you ran this command!!!
## 2. Run usb_cam
<code>roslaunch usb_cam usb_cam-test.launch</code> <br>
Do not close the terminal in which you ran this command!!!
## 3. Run dso ros
Everything as described in the DSO project - only this is for real-time camera input.


		rosrun dso_ros dso_live image:=image_raw \
			calib=XXXXX/camera.txt \
			gamma=XXXXX/pcalib.txt \
			vignette=XXXXX/vignette.png \


## 3.1 Accessing Data.
See the DSO Readme. As of now, there is no default ROS-based `Output3DWrapper` - you will have to write your own.

# 4 Dependencies

## 4.1 Pangolin
removing

	    fullSystem->outputWrapper = new IOWrap::PangolinDSOViewer(
	    		 (int)undistorter->getSize()[0],
	    		 (int)undistorter->getSize()[1]);

will allow you to use DSO compiled without Pangolin. However, then there is no 3D visualization.
You can also implement your own Output3DWrapper to fit your needs.

## 4.2 OpenCV
you can use DSO compiled without OpenCV. 
In that case, the vignette image will not be read, and no photometric calibration can be used. Also, there will not be any image visualizations / image saving.
You can also implement your own version of ImageRW.h / ImageDisplay.h, instead of the dummies.


### 5 License
This ROS wrapper around DSO is licensed under the GNU General Public License
Version 3 (GPLv3).
For commercial purposes, we also offer a professional version, see
[http://vision.in.tum.de/dso](http://vision.in.tum.de/dso) for details.
