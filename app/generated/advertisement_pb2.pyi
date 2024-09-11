from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Category(_message.Message):
    __slots__ = ("subcategory",)
    SUBCATEGORY_FIELD_NUMBER: _ClassVar[int]
    subcategory: str
    def __init__(self, subcategory: _Optional[str] = ...) -> None: ...

class Title(_message.Message):
    __slots__ = ("ro", "ru")
    RO_FIELD_NUMBER: _ClassVar[int]
    RU_FIELD_NUMBER: _ClassVar[int]
    ro: str
    ru: str
    def __init__(self, ro: _Optional[str] = ..., ru: _Optional[str] = ...) -> None: ...

class Advertisement(_message.Message):
    __slots__ = ("_id", "categories", "title", "type", "posted")
    _ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    POSTED_FIELD_NUMBER: _ClassVar[int]
    _id: str
    categories: Category
    title: Title
    type: str
    posted: float
    def __init__(self, _id: _Optional[str] = ..., categories: _Optional[_Union[Category, _Mapping]] = ..., title: _Optional[_Union[Title, _Mapping]] = ..., type: _Optional[str] = ..., posted: _Optional[float] = ...) -> None: ...

class StoreRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StoreResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class RecordsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("title",)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AggregateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AggregateResponse(_message.Message):
    __slots__ = ("aggregated",)
    class AggregatedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    aggregated: _containers.ScalarMap[str, int]
    def __init__(self, aggregated: _Optional[_Mapping[str, int]] = ...) -> None: ...
