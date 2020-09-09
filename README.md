# How-to-Use-Qualisys-Motion-Capture-System-in-AIMS-Lab
This is a tutorial about using [Qualisys Motion Capture System](https://www.qualisys.com/) in [AIMS Lab](https://engineering.purdue.edu/AIMS). This repo includes the useage and the example codes for Qualisys Python and C++ SDK, the [ROS](https://www.ros.org/) driver, and MATLAB.


# Configurations
1. The configuration settings are all in a JSON file *mocap_config.json*. The changes in *mocap_config.json* affect all the codes in different languages, so you don't have to change them manually in every single file.

2. The following are the meaning of each element.
* *"IP_SERVER"* is the IP address for the desktop which connects to the motion capture system. It shouldn't change.
* *"NAME_SINGLE_BODY"* is the rigid body name you define in [QTM](https://www.qualisys.com/software/qualisys-track-manager/). You can have multiple names in this file. But you need to change your codes accordingly to get data for different rigid bodies.
* *"NAME_FILE_LOADED_QTM"* is the file path to load recorded motion capture data, and stream in real-time. (I need to debug it. - Sept 09, 2020)
* *"FLAG_REALTIME"* is the flag to stream real-time data ("1") or recorded data ("0").
* *"HOST_UDP"* is the IP address of the UDP socket.
* *"PORT_UDP"* is the port number of the UDP socket.
* *"DATA_BYTES_LENGTH_UDP"* is the number of bytes you want to send your data via UDP socket. For example, if I want to send a position in R\^3 and a rotation matrix in R\^(3\*3), there are 12 numbers. If the numbers are all double (float64), each number is 8 bytes and in total is 12\*8=96 bytes. 


# Python
1. Follow the official instructions of [qualisys_python_sdk](https://github.com/qualisys/qualisys_python_sdk) to install the python package. The minimum version of Python is 3.5.3 per [Qualisys SDK for Python's documentation](https://qualisys.github.io/qualisys_python_sdk/index.html). This section also need [numpy](https://numpy.org/) to process the data. If you want to use Python 2 with ROS, please navigate to **ROS** section. The following commands in Ubuntu is an example to install numpy and qualisys_python_sdk. The commands in Windows and MacOS should be similar. It assumes that you already have Python 3 and the latest Python package installer [pip](https://pypi.org/project/pip/). You may need to be administrator to install.
```
$ pip3 install numpy
$ pip3 install qtm
```

2. To get 6-DOF data from Qualisys server and publish it via UDP socket, run the following commands. <MAIN_DIRECTORY> is your local main directory of this repo.
Note that you can run this single script if processing 6-DOF data in this script is available. Otherwise, you can use UDP socket in a separate script.
```
$ cd <MAIN_DIRECTORY>
$ python3 .\python\streaming_6dof_data_python.py
```

3. To subscribe to 6-DOF data via UDP socket:
```
$ cd <MAIN_DIRECTORY>
$ python3 .\python\subscriber_6dof_udp_python.py
```

4. To make multiple devices access to the 6-DOF data, you can use either TCP/IP or UDP socket for communications. More information are available in [Tutorial-About-TCP-IP-and-UDP-Communications](https://github.com/zehuilu/Tutorial-About-TCP-IP-and-UDP-Communications).


# MATLAB
1. [QTM Connect for MATLAB](https://www.qualisys.com/software/matlab/) can stream real-time motion capture data to MATLAB, but I'm not sure if we have that license. However, we can still stream real-time data to MATLAB via UDP socket.

2. Add the whole repo to your MATLAB path.

3. Run *subscriber_6dof_udp_matlab.m*

4. To make multiple devices access to the 6-DOF data, you can use either TCP/IP or UDP socket for communications. More information are available in [Tutorial-About-TCP-IP-and-UDP-Communications](https://github.com/zehuilu/Tutorial-About-TCP-IP-and-UDP-Communications).

**Need to test this section after the wireless router comes. - Sept 09, 2020**


# C++
1. 



# ROS
1. 

