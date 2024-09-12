import strawberry
from typing import Dict


@strawberry.type
class CategoryType:
    subcategory: str


@strawberry.type
class TitleType:
    ro: str
    ru: str


@strawberry.type
class AdvertisementType:
    _id: str
    categories: CategoryType
    title: TitleType
    _type: str
    posted: float


@strawberry.type
class StoreResponseType:
    result: str


@strawberry.type
class AggregateResponseType:
    aggregated: strawberry.scalars.JSON
