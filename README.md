# How-to-Use-Qualisys-Motion-Capture-System
This is a tutorial about how to use [Qualisys Motion Capture System](https://www.qualisys.com/). This repo includes the useage and the example codes for Qualisys Python and C++ SDK, the [ROS](https://www.ros.org/) driver, and MATLAB.


# Configurations
1. The configuration settings are all in a JSON file **mocap_config.json**. The changes in **mocap_config.json** affect all the codes here, so you don't have to change them manually in every single file or compile it everytime after you change the settings.

2. The following are the meaning of each element.
* **"IP_SERVER"** is the IP address for the desktop which connects to the motion capture system. It shouldn't change.
* **"NAME_SINGLE_BODY"** is the rigid body name you define in [QTM](https://www.qualisys.com/software/qualisys-track-manager/). You can have multiple names in this file. But you need to change your codes accordingly to get data for different rigid bodies.
* **"NAME_FILE_LOADED_QTM"** is the file path to load recorded motion capture data, and stream in real-time. **(I need to debug it. - Sept 09, 2020)**
* **"FLAG_REALTIME"** is the flag to stream real-time data ("1") or recorded data ("0").
* **"HOST_UDP"** is the IP address of the UDP socket.
* **"PORT_UDP"** is the port number of the UDP socket.
* **"DATA_BYTES_LENGTH_UDP"** is the number of bytes you want to send your data via UDP socket. For example, if I want to send a position in R\^3 and a rotation matrix in R\^(3\*3), there are 12 numbers. If the numbers are all double (float64), each number is 8 bytes and in total is 12\*8=96 bytes. 

3. Download this repo to your local machine.  **<MAIN_DIRECTORY>** is your local main directory of this repo.
```
$ git clone https://github.com/zehuilu/How-to-Use-Qualisys-Motion-Capture-System-in-AIMS-Lab.git
$ cd <MAIN_DIRECTORY>
```


# Python
1. Follow the instructions of [qualisys_python_sdk](https://github.com/qualisys/qualisys_python_sdk) to install the Python SDK. The minimum version of Python is 3.5.3 per [Qualisys SDK for Python's documentation](https://qualisys.github.io/qualisys_python_sdk/index.html). This section also need [numpy](https://numpy.org/) to process the data. If you want to use Python 2 with ROS, please navigate to **ROS** section. The following commands is an example to install numpy and qualisys_python_sdk. It assumes that you already have Python 3 and the latest Python package installer [pip](https://pypi.org/project/pip/). You may need to be administrator to install.
```
$ pip3 install numpy
$ pip3 install qtm
```

2. To get 6-DOF data from Qualisys server and publish it via UDP socket, run the following commands.
Note that you can only run this script if processing 6-DOF data in this script is available.
```
$ cd <MAIN_DIRECTORY>
$ python3 python/streaming_6dof_data.py
```

3. To subscribe the streaming data, run the following commands. The publisher and the subscriber should share the same network with the motion capture server. To subscribe to 6-DOF data via UDP socket:
```
$ cd <MAIN_DIRECTORY>
$ python3 python/subscriber_6dof_udp.py
```

4. To make multiple devices access to the 6-DOF data, you can use either TCP/IP or UDP socket for communications. More information are available in [Tutorial-About-TCP-IP-and-UDP-Communications](https://github.com/zehuilu/Tutorial-About-TCP-IP-and-UDP-Communications).


# UDP data streaming with Python asyncio
1. 

2. 



# MATLAB
1. [QTM Connect for MATLAB](https://www.qualisys.com/software/matlab/) can stream real-time motion capture data to MATLAB. In addition, we can stream real-time data to MATLAB via UDP socket.

2. Add the whole repo to your MATLAB path.

3. Run a publisher to streaming data. For example,
```
$ cd <MAIN_DIRECTORY>
$ python3 python/streaming_6dof_data.py
```

4. Run **subscriber_6dof_udp_matlab.m**. This can be done from multiple platforms and on different machines, as long as they share the same network with the motion capture server.

5. To make multiple devices access to the 6-DOF data, you can use either TCP/IP or UDP socket for communications. More information are available in [Tutorial-About-TCP-IP-and-UDP-Communications](https://github.com/zehuilu/Tutorial-About-TCP-IP-and-UDP-Communications).


# C++
1. I prefer to use [CMake](https://cmake.org/) to build C++ projects in Linux and Windows.

2. Follow the instructions of [qualisys_cpp_sdk](https://github.com/qualisys/qualisys_cpp_sdk) to download the SDK.
```
$ cd <MAIN_DIRECTORY>
$ git clone https://github.com/qualisys/qualisys_cpp_sdk.git
```

3. Follow the instructions velow to build the package.

For Linux:
```
cd qualisys_cpp_sdk
mkdir build
cd build
cmake .. -DBUILD_EXAMPLES=ON
cmake --build .
```

For Windows, Open Developer Command Prompt for VS:
```
cd /d <YOUR_QUALISYS_CPP_SDK>
mkdir build
cd build
cmake .. -DBUILD_EXAMPLES=ON
MSBuild qualisys_cpp_sdk.sln
.\Debug\RigidBodyStreaming.exe
```

# ROS
To-do

