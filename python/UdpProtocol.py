import asyncio


class UdpProtocol:
    """
    A callable asyncio Datagram Protocol implementation.

    Reference:
        https://docs.python.org/3/library/asyncio-protocol.html#datagram-protocols
        https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint    
    """
    def __init__(self):
        self._packets = asyncio.Queue()

    def connection_made(self, transport):
        print("connection made")

    def datagram_received(self, data, addr):
        self._packets.put_nowait((data, addr))

    # def datagram_received(self, data):
    #     self._packets.put_nowait(data)

    def connection_lost(self, transport):
        print("connection lost")

    async def recvfrom(self):
        return await self._packets.get()
