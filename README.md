# realsense_testing

The purpose of this package is to document the testing that was done when first setting up the Intel realsense camera.
###### Hardware / Software used
- Unbuntu 16.04
- ROS Kinetic
- Intel NUC
- Intel Realsense D435i
###### Installation
Followed instructions at:  
github.com/IntelRealSense/realsense-ros  
- `export ROS_VER=kinetic`
- `sudo apt-get install ros-$ROS_VER-realsense2-camera`
- `sudo apt-get update && upgrade`  
###### Using realsense viewer
Now that the required packages have been istalled, can use realsense viewer with the following command:  
`realsense-viewer`  
The realsense viewer allows us to access the camera and view the output from the camera. I also updated the firmware from within this program.  
###### Using realsense with ROS
The following command will launch the appropriate nodes/drivers to use the realsense in ROS:  
`roslaunch realsense2_camera rs_camera.launch`  
Now you should be able to launch RViz and see that relevent topic data, such as depth images, RGB streams.  
For pointclouds:  
`roslaunch realsense2_camera rs_camera.launch filters:=pointcloud`  
## My script - stream_image.py
This script will launch a ROS node that reads the depth data from the realsense camera. We the use OpenCV to determine what the physical depth in the real world is in relation to the centre pixel of the depth image. This scripts purpose is simply to show how we can use ROS, realsense and OpenCV to determine distance/depth in the real world.  
The commands to execute this script are:  
- `roslaunch realsense2_camera rs_camera.launch`
- `roslaunch realsense_testing stream_image.launch`  
PHD candidate Brendan Halloran provided the base code for this script.
