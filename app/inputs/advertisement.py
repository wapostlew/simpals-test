import strawberry


@strawberry.input
class CategoryInput:
    subcategory: str


@strawberry.input
class TitleInput:
    ro: str
    ru: str


@strawberry.input
class AdvertisementInput:
    _id: str
    categories: CategoryInput
    title: TitleInput
    type: str
    posted: float


@strawberry.input
class SearchRequestInput:
    title: str
