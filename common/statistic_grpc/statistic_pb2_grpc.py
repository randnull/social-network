# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import statistic_pb2 as statistic__pb2


class StatisticServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStatisticByPost = channel.unary_unary(
                '/statistic.StatisticService/GetStatisticByPost',
                request_serializer=statistic__pb2.GetByPostRequest.SerializeToString,
                response_deserializer=statistic__pb2.GetByPostResponse.FromString,
                )
        self.GetPopularPost = channel.unary_unary(
                '/statistic.StatisticService/GetPopularPost',
                request_serializer=statistic__pb2.GetPopularPostRequest.SerializeToString,
                response_deserializer=statistic__pb2.GetPopularPostResponse.FromString,
                )
        self.GetPopularUser = channel.unary_unary(
                '/statistic.StatisticService/GetPopularUser',
                request_serializer=statistic__pb2.NoParams.SerializeToString,
                response_deserializer=statistic__pb2.GetPopularUserResponse.FromString,
                )


class StatisticServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStatisticByPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPopularPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPopularUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatisticServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStatisticByPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatisticByPost,
                    request_deserializer=statistic__pb2.GetByPostRequest.FromString,
                    response_serializer=statistic__pb2.GetByPostResponse.SerializeToString,
            ),
            'GetPopularPost': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPopularPost,
                    request_deserializer=statistic__pb2.GetPopularPostRequest.FromString,
                    response_serializer=statistic__pb2.GetPopularPostResponse.SerializeToString,
            ),
            'GetPopularUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPopularUser,
                    request_deserializer=statistic__pb2.NoParams.FromString,
                    response_serializer=statistic__pb2.GetPopularUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'statistic.StatisticService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StatisticService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStatisticByPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/statistic.StatisticService/GetStatisticByPost',
            statistic__pb2.GetByPostRequest.SerializeToString,
            statistic__pb2.GetByPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPopularPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/statistic.StatisticService/GetPopularPost',
            statistic__pb2.GetPopularPostRequest.SerializeToString,
            statistic__pb2.GetPopularPostResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPopularUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/statistic.StatisticService/GetPopularUser',
            statistic__pb2.NoParams.SerializeToString,
            statistic__pb2.GetPopularUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
