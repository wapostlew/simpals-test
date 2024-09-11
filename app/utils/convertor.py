from typing import TypeVar, Type
from pydantic import BaseModel
from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message

ModelType = TypeVar("ModelType", bound=BaseModel)
_MessageT = TypeVar("_MessageT", bound=Message)


class GrpcMessageConvertor:

    @staticmethod
    def rpc_to_pydantic(model: Type[ModelType], message: Message) -> ModelType:
        return model(
            **MessageToDict(
                message=message,
                preserving_proto_field_name=True,
                use_integers_for_enums=False,
            )
        )

    @staticmethod
    def pydantic_to_rpc(
        data: ModelType, schema: _MessageT, ignore_unknown_fields: bool = True
    ):
        return ParseDict(
            js_dict=data.dict(by_alias=True),
            message=schema,
            ignore_unknown_fields=ignore_unknown_fields,
        )
