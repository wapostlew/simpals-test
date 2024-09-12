from pydantic import BaseModel, ConfigDict, Field


class Category(BaseModel):
    subcategory: str


class Title(BaseModel):
    ro: str
    ru: str


class Advertisement(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id_: str = Field(alias="_id")
    categories: Category
    title: Title
    type_: str = Field(alias="type")
    posted: float


class StoreResponse(BaseModel):
    result: str


class SearchRequest(BaseModel):
    title: str


class AggregateResponse(BaseModel):
    aggregated: dict[str, int] = {}
