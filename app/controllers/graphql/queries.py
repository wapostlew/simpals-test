import os
import strawberry
from app.clients.advertisement import AdvertisementClient
from app.types import advertisement as ad_types


@strawberry.type
class Query:
    @strawberry.field
    async def get_advertisement_aggregate(self) -> ad_types.AggregateResponseType:
        advertisement_grpc_client = AdvertisementClient(
            host=os.getenv("GRPC_CLIENT_ADS_HOST", "localhost"),
            port=int(os.getenv("GRPC_CLIENT_ADS_PORT", 50050)),
        )
        response = await advertisement_grpc_client.aggregate()
        return ad_types.AggregateResponseType(aggregated=response.aggregated)
