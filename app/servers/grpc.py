import concurrent.futures
import grpc
import logging
from app import configs
from app.generated import advertisement_pb2_grpc
from app.controllers.grpc import advertisement


logging.basicConfig(level=logging.DEBUG)


async def serve():
    server = grpc.aio.server(concurrent.futures.ThreadPoolExecutor())
    advertisement_pb2_grpc.add_AdvertisementServiceServicer_to_server(
        advertisement.AdvertisementServicer(), server
    )

    server.add_insecure_port(f"{configs.grpc.host}:{configs.grpc.port}")
    logging.info(
        f"Server started, listening on {configs.grpc.host}:{configs.grpc.port}"
    )
    print(f"Server started, listening on {configs.grpc.host}:{configs.grpc.port}")
    await server.start()

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server stopped!")
    finally:
        await server.stop(grace=5.0)


if __name__ == "__main__":
    import asyncio

    asyncio.run(serve())
