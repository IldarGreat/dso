if [ ! -f /opt/ros/noetic/setup.bash ]; then
	echo "Script setup not found!"
	DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
	echo "$DIR"
	exit 1
else
	cd /user_ws
	source devel/setup.bash
	echo "Sourced setup.bash of workspace"
	source /opt/ros/noetic/setup.bash
	echo "Sourced setup.bash of ros"
	roscore & roslaunch --wait usb_cam usb_cam-test.launch & sleep 15
fi
catkin clean
catkin_make
source /user_ws/devel/setup.bash
source devel/setup.bash
echo "All working topics:"
rostopic list
echo "Starting dso ros..."
rosrun dso_ros dso_live image:=/usb_cam/image_raw calib=/user_ws/camera/camera.txt nogui=1
