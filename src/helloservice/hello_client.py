import logging
import asyncio
import grpc

import ms_pb2_grpc
import ms_pb2


async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:8080') as channel:
        stub = ms_pb2_grpc.HelloStub(channel)
        response = await stub.SayHello(
            ms_pb2.SayHelloRequest(name="test")
            )
    print("Hello client recieved: "+ response.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())