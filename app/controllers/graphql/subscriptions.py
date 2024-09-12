import strawberry
from typing import AsyncGenerator
from app.clients.advertisement import AdvertisementClient
from app.types import advertisement as ad_types
from app.inputs import advertisement as ad_inputs
from app.schemas import advertisement as ad_schemas
from app.configs import graphql as gql_config


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def search_advertisement(
        self, input_: ad_inputs.SearchRequestInput
    ) -> AsyncGenerator[ad_types.AdvertisementType, None]:
        advertisement_grpc_client = AdvertisementClient(
            host=gql_config.clients.grpc.avertisement.host,
            port=gql_config.clients.grpc.avertisement.port,
        )
        async for item in advertisement_grpc_client.search(
            query=ad_schemas.SearchRequest(**strawberry.asdict(input_))
        ):
            yield ad_types.AdvertisementType(**item.dict(by_alias=True))

    @strawberry.subscription
    async def get_all_advertisement(
        self,
    ) -> AsyncGenerator[ad_types.AdvertisementType, None]:
        advertisement_grpc_client = AdvertisementClient(
            host=gql_config.clients.grpc.avertisement.host,
            port=gql_config.clients.grpc.avertisement.port,
        )
        async for item in advertisement_grpc_client.records():
            yield ad_types.AdvertisementType(**item.dict(by_alias=True))
