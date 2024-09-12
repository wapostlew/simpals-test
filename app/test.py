import asyncio
import json
from app.clients.advertisement import AdvertisementClient
from app.schemas.advertisement import Advertisement


async def test_req():
    client = AdvertisementClient(port=51500)
    # values = json.load(open("data/advertisement.json"))
    # for item in values:
    # print(await client.store(data=Advertisement(**item)))
    async for result in client.records():
        print(result)
    print(await client.aggregate())
    return True


asyncio.run(test_req())
