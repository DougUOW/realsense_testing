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
