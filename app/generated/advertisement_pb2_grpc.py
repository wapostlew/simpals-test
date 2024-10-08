# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import app.generated.advertisement_pb2 as advertisement__pb2

GRPC_GENERATED_VERSION = "1.66.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in advertisement_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class AdvertisementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Store = channel.unary_unary(
            "/advertisement.AdvertisementService/Store",
            request_serializer=advertisement__pb2.Advertisement.SerializeToString,
            response_deserializer=advertisement__pb2.StoreResponse.FromString,
            _registered_method=True,
        )
        self.Records = channel.unary_stream(
            "/advertisement.AdvertisementService/Records",
            request_serializer=advertisement__pb2.RecordsRequest.SerializeToString,
            response_deserializer=advertisement__pb2.Advertisement.FromString,
            _registered_method=True,
        )
        self.Search = channel.unary_stream(
            "/advertisement.AdvertisementService/Search",
            request_serializer=advertisement__pb2.SearchRequest.SerializeToString,
            response_deserializer=advertisement__pb2.Advertisement.FromString,
            _registered_method=True,
        )
        self.Aggregate = channel.unary_unary(
            "/advertisement.AdvertisementService/Aggregate",
            request_serializer=advertisement__pb2.AggregateRequest.SerializeToString,
            response_deserializer=advertisement__pb2.AggregateResponse.FromString,
            _registered_method=True,
        )


class AdvertisementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Store(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Records(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Aggregate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AdvertisementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Store": grpc.unary_unary_rpc_method_handler(
            servicer.Store,
            request_deserializer=advertisement__pb2.Advertisement.FromString,
            response_serializer=advertisement__pb2.StoreResponse.SerializeToString,
        ),
        "Records": grpc.unary_stream_rpc_method_handler(
            servicer.Records,
            request_deserializer=advertisement__pb2.RecordsRequest.FromString,
            response_serializer=advertisement__pb2.Advertisement.SerializeToString,
        ),
        "Search": grpc.unary_stream_rpc_method_handler(
            servicer.Search,
            request_deserializer=advertisement__pb2.SearchRequest.FromString,
            response_serializer=advertisement__pb2.Advertisement.SerializeToString,
        ),
        "Aggregate": grpc.unary_unary_rpc_method_handler(
            servicer.Aggregate,
            request_deserializer=advertisement__pb2.AggregateRequest.FromString,
            response_serializer=advertisement__pb2.AggregateResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "advertisement.AdvertisementService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "advertisement.AdvertisementService", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class AdvertisementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Store(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/advertisement.AdvertisementService/Store",
            advertisement__pb2.Advertisement.SerializeToString,
            advertisement__pb2.StoreResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Records(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/advertisement.AdvertisementService/Records",
            advertisement__pb2.RecordsRequest.SerializeToString,
            advertisement__pb2.Advertisement.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Search(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/advertisement.AdvertisementService/Search",
            advertisement__pb2.SearchRequest.SerializeToString,
            advertisement__pb2.Advertisement.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Aggregate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/advertisement.AdvertisementService/Aggregate",
            advertisement__pb2.AggregateRequest.SerializeToString,
            advertisement__pb2.AggregateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
