import asyncio
import grpc
from app import configs
from app.generated import advertisement_pb2_grpc
from app.controllers.grpc import advertisement


async def serve():
    server = grpc.aio.server()
    advertisement_pb2_grpc.add_AdvertisementServiceServicer_to_server(
        advertisement.AdvertisementServicer(), server
    )

    server.add_insecure_port(f"{configs.grpc.host}:{configs.grpc.port}")

    await server.start()
    print(f"Server started, listening on {configs.grpc.host}:{configs.grpc.port}")
    await server.wait_for_termination(15)


if __name__ == "__main__":
    asyncio.run(serve())
