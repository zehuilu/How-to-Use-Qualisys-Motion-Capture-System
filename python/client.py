#!/usr/bin/env python3

import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port).
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie
# client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# # Enable broadcasting mode
# client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
while True:

    newestData = None

    keepReceiving = True
    while keepReceiving:
        try:
            data, fromAddr = client.recvfrom(4096)
            if data:
                newestData = data

            print("check")
            print(data)

        except socket.error as why:
            if why.args[0] == EWOULDBLOCK:
                keepReceiving = False
            else:
                raise why

    if (newestData):
        # code to handle/parse (newestData) here
        print(data)

    time.sleep(1)

