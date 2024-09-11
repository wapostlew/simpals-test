from typing import AsyncGenerator
from elasticsearch import AsyncElasticsearch
from app.schemas import advertisement as ad_schema


class AdvertisementManager:
    def __init__(self, client: AsyncElasticsearch):
        self.index_name = "advertisement"
        self.es = client

    @staticmethod
    def mapping():
        return {
            "properties": {
                "categories": {"properties": {"subcategory": {"type": "keyword"}}},
                "title": {
                    "properties": {
                        "ro": {"type": "text", "analyzer": "standard"},
                        "ru": {"type": "text", "analyzer": "standard"},
                    }
                },
                "type": {"type": "keyword"},
                "posted": {"type": "date"},
            }
        }

    async def store(self, data: ad_schema.Advertisement) -> ad_schema.StoreResponse:
        response = await self.es.index(
            index=self.index_name,
            id=data.id_,
            body=data.dict(by_alias=True, exclude={"id_"}),
        )
        return ad_schema.StoreResponse(result=response["result"])

    async def records(self) -> AsyncGenerator[ad_schema.Advertisement, None]:
        response = await self.es.search(
            index=self.index_name,
            body={
                "size": 100,
                "query": {
                    "match_all": {},
                },
            },
            scroll="1m",
        )

        while len(response["hits"]["hits"]):
            for hit in response["hits"]["hits"]:
                yield ad_schema.Advertisement(
                    **{
                        "_id": hit["_id"],
                        **hit["_source"],
                    }
                )
            response = await self.es.scroll(
                scroll_id=response["_scroll_id"], scroll="1m"
            )
        await self.es.clear_scroll(scroll_id=response["_scroll_id"])

    async def search(
        self, query: ad_schema.SearchRequest
    ) -> AsyncGenerator[ad_schema.Advertisement, None]:
        response = await self.es.search(
            index=self.index_name,
            body={
                "query": {
                    "multi_match": {"query": query.title, "fields": ["title.*"]},
                },
            },
        )
        for hit in response["hits"]["hits"]:
            yield ad_schema.Advertisement(
                **{
                    "_id": hit["_id"],
                    **hit["_source"],
                }
            )

    async def aggregate(self) -> ad_schema.AggregateResponse:
        response = await self.es.search(
            index=self.index_name,
            body={
                "size": 0,
                "aggs": {
                    "subcategories": {
                        "terms": {
                            "field": "categories.subcategory",
                        },
                    },
                },
            },
        )
        return ad_schema.AggregateResponse(
            aggregated={
                bucket["key"]: bucket["doc_count"]
                for bucket in response["aggregations"]["subcategories"]["buckets"]
            }
        )
