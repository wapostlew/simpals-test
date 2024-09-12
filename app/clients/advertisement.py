from typing import AsyncGenerator
import grpc
from app import configs
from app.generated import advertisement_pb2, advertisement_pb2_grpc
from app.schemas import advertisement as ad_schema
from app.utils.convertor import GrpcMessageConvertor


class AdvertisementClient:
    def __init__(self, host: str = "localhost", port: int = configs.grpc.port):
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = advertisement_pb2_grpc.AdvertisementServiceStub(self.channel)
        self.convertor = GrpcMessageConvertor()

    async def store(self, data: ad_schema.Advertisement) -> ad_schema.StoreResponse:
        response = await self.stub.Store(
            self.convertor.pydantic_to_rpc(
                data=data, schema=advertisement_pb2.Advertisement()
            )
        )
        return self.convertor.rpc_to_pydantic(
            model=ad_schema.StoreResponse, message=response
        )

    async def records(self) -> AsyncGenerator[ad_schema.Advertisement, None]:
        response = self.stub.Records(advertisement_pb2.RecordsRequest())

        async for item in response:
            yield self.convertor.rpc_to_pydantic(
                model=ad_schema.Advertisement,
                message=item,
            )

    async def search(
        self,
        query: ad_schema.SearchRequest,
    ) -> AsyncGenerator[ad_schema.Advertisement, None]:
        response = self.stub.Search(
            self.convertor.pydantic_to_rpc(
                data=query, schema=advertisement_pb2.SearchRequest()
            )
        )

        async for item in response:
            yield self.convertor.rpc_to_pydantic(
                model=ad_schema.Advertisement,
                message=item,
            )

    async def aggregate(self) -> ad_schema.AggregateResponse:
        response = await self.stub.Aggregate(advertisement_pb2.AggregateRequest())
        return self.convertor.rpc_to_pydantic(
            model=ad_schema.AggregateResponse,
            message=response,
        )
