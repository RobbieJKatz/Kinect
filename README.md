# **Kinect**

## SUMMARY

This project details the installation and the programming of the Microsoft Kinect using Libfreenect, OpenNI, NITE as well as PyOpenNI on an ubuntu-15.10 system. 

## Installation

The installation of all the files was done on a clean install of ubuntu-15.10. There is no guarantee that this would work on other distributions especially versions of Ubuntu earlier than Ubuntu 10.x. It also seems that installation instructions have a lifespan, so these instructions may no longer be valid in the future. They do work as of 28 March 2017. 

**sudo apt-get update**

**sudo apt-get install git-core cmake python-dev python-numpy freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev libgtk2.0-dev doxygen graphviz**

**mkdir ~/kinect**  
**cd ~/kinect** 

**git clone https://github.com/OpenKinect/libfreenect**    
**git clone https://github.com/OpenNI/OpenNI**    
**git clone https://github.com/avin2/SensorKinect**

### Installing Libfreenect
**cd ~/kinect/libfreenect**  
**mkdir build**  
**cd build**  
**cmake ..**  
**make**  
**sudo make install***  
**sudo ldconfig /usr/local/lib64/***

To ensure that Libfreenect has been installed correctly, connect your kinect and run:     
***sudo freenect-glview***  
and you should see the infrared and camera view from the kinect. 

Now install java:  
***sudo apt-get install default-jdk***

### Installing OpenNI
**cd ~/kinect/OpenNI**  
**git checkout Unstable-1.5.4.0**  
**cd Platform/Linux/CreateRedist**  
**chmod +x RedistMaker**  
**./RedistMaker**  
**cd ../Redist/Sensor-Bin-Linux-x64-v5.1.2.1/**  
**sudo ./install.sh**

If you do not run the checkout command the next set of instructions will not work. 

### Installing SensorKinect
**cd ~/kinect/SensorKinect/Platform/Linux/CreateRedist**  
**chmod +x RedistMaker**  
**./RedistMaker**  
**cd ../Redist/Sensor-Bin-Linux-x64-v5.1.2.1**  
**chmod +x install.sh**  
**sudo ./install.sh**

At this point some of the OpenNI examples will work. If you look in the ~/kinect/OpenNI/Platform/Linux/Bin/x64-Release folder you will see some examples that can be executed. Running **./Sample-NiSimpleViewer** should run the one example. The other examples won’t work until we install NITE. 

### Installing NITE
download Nite from https://code.google.com/archive/p/simple-openni/downloads and unzip the package and put it in ~/kinect    
go to the folder ~/kinect/OpenNI_NITE_Installer-Linux64-0.27/NITE-Bin-Dev-Linux-x64-v1.5.2.21/Data/ and edit the 3 XML files.  
In each replace the appropriate line to **<vendor="PrimeSense" key="0KOIk2JeIBYClPWVnMoRKn5cdY4=“>**. 

**./install.sh**  
**niLicense PrimeSense 0KOIk2JeIBYClPWVnMoRKn5cdY4=**  
** niLicense -l**

can try to interchange those instructions…

Now check that the rest of the examples from OpenNI work (~/kinect/OpenNI/Platform/Linux/Bin/x64-Release). These are binary files (or whatever) and cannot be edited. The files that can be edited are in ~/kinect/OpenNI/Samples  
It is possible to edit these files and the compile them by going to ~/kinect/OpenNI/Platform/Linux/Build and running **make** which compiles the files to the ~/kinect/OpenNI/Platform/Linux/Bin/x64-Release folder. But who wants to do that when you can code in Python? 

### Installing PyOpenNI

 
