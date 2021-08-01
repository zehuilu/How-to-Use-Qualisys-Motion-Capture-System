import asyncio
from UdpProtocol import UdpProtocol


async def main():

    

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        UdpProtocol,
        local_addr=None,
        remote_addr=('127.0.0.1', 8000))

    idx = 0
    while True:
        transport.sendto(str(idx).encode(), ('127.0.0.1', 8000))
        print(idx)
        idx += 1
        await asyncio.sleep(0.1)

asyncio.run(main())
