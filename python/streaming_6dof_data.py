#!/usr/bin/python3

"""
    Streaming 6-DOF data from QTM forever
    (start QTM first, Capture->Continuous Capture)
"""

import asyncio
import xml.etree.ElementTree as ET
import pkg_resources
import qtm
import json
import numpy as np
import socket


def create_body_index(xml_string):
    """ Extract a name to index dictionary from 6-DOF settings xml """
    xml = ET.fromstring(xml_string)

    body_to_index = {}
    for index, body in enumerate(xml.findall("*/Body/Name")):
        body_to_index[body.text.strip()] = index

    return body_to_index


def publisher_udp_main(json_file_data):
    """
    The following two lines show what is json_file_data

        json_file = open('mocap_config.json')
        json_file_data = json.load(json_file)
    """

    # IP for publisher
    HOST_UDP = json_file_data['HOST_UDP']
    # Port for publisher
    PORT_UDP = int(json_file_data['PORT_UDP'])

    server_address_udp = (HOST_UDP, PORT_UDP)
    # Create a UDP socket
    sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    return sock_udp, server_address_udp


async def main(network_config_file_name):
    # Read the configuration from the json file
    json_file = open(network_config_file_name)
    json_file_data = json.load(json_file)

    # 1 for realtime streaming, 0 for loading qtm file
    flag_realtime = int(json_file_data['FLAG_REALTIME'])

    # IP address for the mocap server
    IP_server = json_file_data['IP_SERVER']

    # If you want to stream recorded data in a real-time way, change json file and load it here.
    # There might be a bug about file path. Will test it later. -- Sept. 08, 2020
    file_name_qtm = json_file_data['NAME_FILE_LOADED_QTM']
    QTM_FILE = pkg_resources.resource_filename("qtm", file_name_qtm)

    # Connect to qtm
    connection = await qtm.connect(IP_server)

    # Connection failed?
    if connection is None:
        print("Failed to connect")
        return

    # Take control of qtm, context manager will automatically release control after scope end
    async with qtm.TakeControl(connection, "password"):
        if not flag_realtime:
            # Load qtm file
            await connection.load(QTM_FILE)
            # start rtfromfile
            await connection.start(rtfromfile=True)

    # Get 6-DOF settings from QTM
    xml_string = await connection.get_parameters(parameters=["6d"])

    # Create a UDP socket for data streaming
    sock_udp, server_address_udp = publisher_udp_main(json_file_data)

    # parser for mocap rigid bodies indexing
    body_index = create_body_index(xml_string)

    wanted_body = json_file_data['NAME_SINGLE_BODY']

    def on_packet(packet):
        # Get the 6-DOF data
        bodies = packet.get_6d()[1]

        if wanted_body is not None and wanted_body in body_index:
            # Extract one specific body
            wanted_index = body_index[wanted_body]
            position, rotation = bodies[wanted_index]
            # You can use position and rotation here. Notice that the unit for position is mm!
            print(wanted_body)

            print("Position in numpy [meter]")
            position_np = np.array([[position.x/1000.0], [position.y/1000.0], [position.z/1000.0]], dtype=np.float64)
            print(position_np)

            # rotation.matrix is a tuple with 9 elements.
            print("Rotation matrix in numpy")
            rotation_np = np.asarray(rotation.matrix, dtype=np.float64).reshape(3, 3)
            print(rotation_np)

            # send 6-DOF data via UDP
            # concatenate the position and rotation matrix vertically
            msg = np.asarray((position.x/1000.0, position.y/1000.0, position.z/1000.0) + rotation.matrix, dtype=np.float64).tobytes()
            sock_udp.sendto(msg, server_address_udp)
            print("6-DOF data sent via UDP!")
        
        else:
            # Print all bodies
            for position, rotation in bodies:
                print("There is no such a rigid body! Print all bodies.")
                print("Pos: {} - Rot: {}".format(position, rotation))

    # Start streaming frames
    # Make sure the component matches with the data fetch function, for example: packet.get_6d() with "6d"
    # Reference: https://qualisys.github.io/qualisys_python_sdk/index.html
    await connection.stream_frames(components=["6d"], on_packet=on_packet)


if __name__ == "__main__":
    network_config_file_name = 'mocap_config.json'
    # Run our asynchronous main function forever
    asyncio.ensure_future(main(network_config_file_name))
    asyncio.get_event_loop().run_forever()