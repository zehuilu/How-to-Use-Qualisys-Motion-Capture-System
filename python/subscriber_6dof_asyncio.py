#!/usr/bin/python3
import socket
import time
import json
import numpy as np
import threading

"""
    This is an example where you can launch a subscriber via UDP.
    You can receive data from the specific IP address and port you define.
"""

async def subscriber_udp_main(network_config_file_name):

    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # IP for listening data
    HOST = json_file_data['HOST_UDP']
    # Port for listening data
    PORT = int(json_file_data['PORT_UDP'])
    server_address = (HOST, PORT)

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        UdpProtocol, local_addr=server_address, remote_addr=None)

    while True:
        await subscriber_callback(protocol)
        await asyncio.sleep(1.0)

def subscriber_callback(protocol):
    """
    Receives the data from the publisher.
    """

    msg = await protocol.recvfrom()

    data = np.frombuffer(msg, dtype=np.float64)
    # print("Received the data from the publisher.")
    # print(data)

    position = np.array([[data[0]], [data[1]], [data[2]]], dtype=np.float64)
    rotation = np.asarray(data[3:], dtype=np.float64).reshape(3, 3)

    print("Position in numpy [meter]")
    print(position)
    # print("Rotation matrix in numpy")
    # print(rotation)


if __name__ == "__main__":
    network_config_file_name = 'mocap_config.json'
    asyncio.run(subscriber_udp_main(network_config_file_name))
