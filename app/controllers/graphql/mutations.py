import strawberry
from app.clients.advertisement import AdvertisementClient
from app.types import advertisement as ad_types
from app.inputs import advertisement as ad_inputs
from app.schemas import advertisement as ad_schemas
from app.configs import graphql as gql_config


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_advertisement(
        self, input_: ad_inputs.AdvertisementInput
    ) -> ad_types.StoreResponseType:
        advertisement_grpc_client = AdvertisementClient(
            host=gql_config.clients.grpc.avertisement.host,
            port=gql_config.clients.grpc.avertisement.port,
        )
        response = await advertisement_grpc_client.store(
            data=ad_schemas.Advertisement(
                **strawberry.asdict(input_),
            )
        )
        return ad_types.StoreResponseType(**response.dict(by_alias=True))
