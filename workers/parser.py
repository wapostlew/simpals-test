import os
import asyncio
import ijson
from app.clients.advertisement import AdvertisementClient
from app.schemas import advertisement as ad_schemas


async def parser():
    client = AdvertisementClient(
        host=os.getenv("GRPC_CLIENT_ADS_HOST", "localhost"),
        port=os.getenv("GRPC_CLIENT_ADS_PORT", 50050),
    )

    with open("data/advertisement.json", "rb") as f:
        for item in ijson.items(f, "item"):
            response = await client.store(data=ad_schemas.Advertisement(**item))
            print(response.result)


if __name__ == "__main__":
    asyncio.run(parser())
