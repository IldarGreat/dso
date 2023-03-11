source /opt/ros/noetic/setup.bash
cd app/dso/build
./bin/dso_dataset
cd ../../..
cd user_ws/src

# Move dso dir to workspace packages
catkin_init_workspace

cd ..
mv /user_ws/src/Pangolin /opt
mv /user_ws/src/dso /opt
ls src
catkin_make

source /user_ws/devel/setup.bash

rospack find dso_ros
