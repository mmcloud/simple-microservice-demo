import logging
import asyncio
import grpc
import ms_pb2
import ms_pb2_grpc
import os

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

class Hello(ms_pb2_grpc.HelloServicer):

    async def SayHello(
        self, 
        request: ms_pb2.SayHelloRequest,
        context: grpc.aio.ServicerContext
        ) -> ms_pb2.SayHelloResponse:
        logging.info("say hello called")
        return ms_pb2.SayHelloResponse(message=f"hello {request.name}")

    async def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING)

    async def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED)

async def serve() -> None:
    server = grpc.aio.server()
    service = Hello()
    ms_pb2_grpc.add_HelloServicer_to_server(service, server)
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
    port = os.environ.get('PORT', "8080")
    listen_addr = '[::]:' + port
    logging.info("listening on port: " + port)
    server.add_insecure_port(listen_addr)
    logging.info(f"starting server on {listen_addr}")
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        await server.stop(0)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())