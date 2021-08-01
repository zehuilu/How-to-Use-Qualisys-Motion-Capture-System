import asyncio
from UdpProtocol import UdpProtocol


async def main():


    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        UdpProtocol,
        local_addr=('127.0.0.1', 8000),
        remote_addr=None)

    while True:
        data, addr = await protocol.recvfrom()
        print(data, addr)
        # data = await protocol.recvfrom()
        # print(data)
        await asyncio.sleep(2)

asyncio.run(main())