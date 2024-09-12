import os
import concurrent.futures
import grpc
import logging
from app.generated import advertisement_pb2_grpc
from app.controllers.grpc import advertisement


logging.basicConfig(level=logging.DEBUG)


async def serve():
    es_url = "".join(
        [
            os.getenv("SERVICE_GRPC_DB_ELASTICSEARCH_SCHEMA", "http"),
            "://",
            os.getenv("SERVICE_GRPC_DB_ELASTICSEARCH_HOST", "localhost"),
            ":",
            os.getenv("SERVICE_GRPC_DB_ELASTICSEARCH_PORT", "9200"),
        ]
    )
    logging.info(f"ES URL: {es_url}")
    server = grpc.aio.server(concurrent.futures.ThreadPoolExecutor())
    advertisement_pb2_grpc.add_AdvertisementServiceServicer_to_server(
        advertisement.AdvertisementServicer(es_url=es_url), server
    )
    host, port = os.getenv("SERVICE_GRPC_HOST", "[::]"), int(
        os.getenv("SERVICE_GRPC_PORT", 50050)
    )
    server.add_insecure_port(f"{host}:{port}")
    logging.info(f"Server started, listening on {host}:{port}")
    print(f"Server started, listening on {host}:{port}")
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
