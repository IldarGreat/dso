FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update 
RUN apt-get install -y git build-essential libsuitesparse-dev libeigen3-dev libboost-all-dev libopencv-dev 
WORKDIR /app
RUN git clone https://github.com/IldarGreat/dso.git

WORKDIR /app
RUN git clone --recursive https://github.com/stevenlovegrove/Pangolin.git -b v0.6
WORKDIR /app/Pangolin
RUN apt-get install -y cmake
RUN apt-get clean
RUN apt install -y libglew-dev
RUN apt-get install -y libegl1-mesa-dev

RUN cmake -B build && \
    cmake --build build

RUN apt-get install -y zlib1g-dev
WORKDIR /app/dso/thirdparty
RUN tar -zxvf libzip-1.1.1.tar.gz
WORKDIR /app/dso/thirdparty/libzip-1.1.1/
RUN ./configure && \
    make && \
    cp lib/zipconf.h /usr/local/include/zipconf.h

RUN git submodule update --init
WORKDIR /app/dso/build
RUN cmake .. && \
    make

WORKDIR /
COPY launchd.sh .
RUN "./launchd.sh"

WORKDIR /user_ws/src
RUN git clone -b catkin https://github.com/JakobEngel/dso_ros.git
WORKDIR /

RUN "./launchd.sh"

RUN apt-get update
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-get install -y curl gnupg
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN apt-get update 
RUN apt-get install -y ros-noetic-ros-base ros-noetic-usb-cam ros-noetic-cv-bridge 
    
RUN "./launchd.sh"

COPY SampleOutputWrapper.h /user_ws/src/dso/src/IOWrapper/OutputWrapper
COPY CMakeLists.txt /user_ws/src/dso_ros
COPY main.cpp /user_ws/src/dso_ros/src
COPY init.bashrc .

RUN "./launchd.sh"

RUN bash -c 'source init.bashrc'

COPY launch.bashrc .
ENTRYPOINT /bin/bash -c 'source launch.bashrc'


