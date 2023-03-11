/**
* This file is part of DSO.
* 
* Copyright 2016 Technical University of Munich and Intel.
* Developed by Jakob Engel <engelj at in dot tum dot de>,
* for more information see <http://vision.in.tum.de/dso>.
* If you use this code, please cite the respective publications as
* listed on the above website.
*
* DSO is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* DSO is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with DSO. If not, see <http://www.gnu.org/licenses/>.
*/


#pragma once
#include "boost/thread.hpp"
#include "util/MinimalImage.h"
#include "IOWrapper/Output3DWrapper.h"

#include <ros/ros.h>
#include <std_msgs/String.h>

#include "FullSystem/HessianBlocks.h"
#include "util/FrameShell.h"

namespace dso
{

class FrameHessian;
class CalibHessian;
class FrameShell;


namespace IOWrap
{

class SampleOutputWrapper : public Output3DWrapper
{
public:
	ros::Publisher str_pub;
        inline SampleOutputWrapper()
        {
            ros::NodeHandle nh;
            str_pub = nh.advertise<std_msgs::String>("cam_pub",1000);
            printf("OUT: Created ROS OutputWrapper!\n");
        }

        virtual ~SampleOutputWrapper()
        {
            printf("OUT: Destroyed ROS OutputWrapper\n");
        }

        virtual void publishGraph(const std::map<uint64_t, Eigen::Vector2i, std::less<uint64_t>, Eigen::aligned_allocator<std::pair<const uint64_t, Eigen::Vector2i>>> &connectivity) override
        {
           
        }



        virtual void publishKeyframes( std::vector<FrameHessian*> &frames, bool final, CalibHessian* HCalib) override
        {
           
        }

        virtual void publishCamPose(FrameShell* frame, CalibHessian* HCalib) override
        {
        	std::ostringstream oss;
        	oss << frame->timestamp <<
			" " << frame->camToWorld.translation().transpose()<<
			" " << frame->camToWorld.so3().unit_quaternion().x()<<
			" " << frame->camToWorld.so3().unit_quaternion().y()<<
			" " << frame->camToWorld.so3().unit_quaternion().z()<<
			" " << frame->camToWorld.so3().unit_quaternion().w() << "\n";
	 	std::string string_frame = oss.str();
	 	std_msgs::String msg;
	 	msg.data = string_frame;
	 	str_pub.publish(msg);
	 	ros::spinOnce();
	 	ROS_INFO(string_frame);
        }


        virtual void pushLiveFrame(FrameHessian* image) override
        {
            // can be used to get the raw image / intensity pyramid.
        }

        virtual void pushDepthImage(MinimalImageB3* image) override
        {
            // can be used to get the raw image with depth overlay.
        }
        virtual bool needPushDepthImage() override
        {
            return false;
        }

        virtual void pushDepthImageFloat(MinimalImageF* image, FrameHessian* KF ) override
        {
           
        }


};



}



}
