# How-to-Use-Qualisys-Motion-Capture-System-in-AIMS-Lab
This is a tutorial about using Qualisys Motion Capture System in AIMS Lab. This repo includes the useage and the example codes for Qualisys Python and C++ SDK, as well as the ROS driver.

**Python:**
1. Follow the official instructions of [qualisys_python_sdk](https://github.com/qualisys/qualisys_python_sdk) to install the python package. The minimum version of Python is 3.5.3 per [Qualisys SDK for Python's documentation](https://qualisys.github.io/qualisys_python_sdk/index.html). If you want to use Python 2 with [ROS](https://www.ros.org/), please navigate to **ROS** section.

2. The configuration settings are all in *mocap_config.json*.

3. To get 6-DOF data from Qualisys server and publish it via UDP socket: (Assume you are in the main directory.)
Note that you can only run this script if processing 6-DOF data in this script is available.
```
$ python3 .\python\streaming_6dof_data.py
```

4. To subscribe to 6-DOF data via UDP socket:
```
$ python3 .\python\subscriber_6dof_udp.py
```

5. To make multiple devices access to the 6-DOF data, you can use either TCP/IP or UDP socket for communications. More information are available in [Tutorial-About-TCP-IP-and-UDP-Communications](https://github.com/zehuilu/Tutorial-About-TCP-IP-and-UDP-Communications).

