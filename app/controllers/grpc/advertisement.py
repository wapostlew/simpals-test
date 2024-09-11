from elasticsearch import AsyncElasticsearch
from app.configs import grpc
from app.generated import advertisement_pb2, advertisement_pb2_grpc
from app.schemas import advertisement as ad_schema
from app.managers.advertisement import AdvertisementManager
from app.helpers.checker import initialize_mappings
from app.utils.convertor import GrpcMessageConvertor


class AdvertisementServicer(advertisement_pb2_grpc.AdvertisementServiceServicer):
    def __init__(self):
        self.convertor = GrpcMessageConvertor()
        self.mannager = AdvertisementManager(
            AsyncElasticsearch(
                hosts=grpc.db.elasticsearch.unicode_string(),
            )
        )

        initialize_mappings(
            grpc.db.elasticsearch.unicode_string(),
            self.mannager.index_name,
            self.mannager.mapping(),
        )

    async def Store(self, request, context):
        result = await self.mannager.store(
            data=self.convertor.rpc_to_pydantic(
                model=ad_schema.Advertisement,
                message=request,
            )
        )
        return self.convertor.pydantic_to_rpc(
            data=result,
            schema=advertisement_pb2.StoreResponse(),
        )

    async def Records(self, request, context):
        async for item in self.mannager.records():
            yield self.convertor.pydantic_to_rpc(
                data=item,
                schema=advertisement_pb2.Advertisement(),
            )

    async def Search(self, request, context):
        async for item in self.mannager.search(
            query=self.convertor.rpc_to_pydantic(
                model=ad_schema.SearchRequest,
                message=request,
            )
        ):
            yield self.convertor.pydantic_to_rpc(
                data=item,
                schema=advertisement_pb2.Advertisement(),
            )

    async def Aggregate(self, request, context):
        result = await self.mannager.aggregate()
        return self.convertor.pydantic_to_rpc(
            data=result,
            schema=advertisement_pb2.AggregateResponse(),
        )
