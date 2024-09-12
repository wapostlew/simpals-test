import strawberry
from app.clients.advertisement import AdvertisementClient
from app.types import advertisement as ad_types
from app.configs import graphql as gql_config


@strawberry.type
class Query:
    @strawberry.field
    async def get_advertisement_aggregate(self) -> ad_types.AggregateResponseType:
        advertisement_grpc_client = AdvertisementClient(
            host=gql_config.clients.grpc.avertisement.host,
            port=gql_config.clients.grpc.avertisement.port,
        )
        response = await advertisement_grpc_client.aggregate()
        return ad_types.AggregateResponseType(aggregated=response.aggregated)
