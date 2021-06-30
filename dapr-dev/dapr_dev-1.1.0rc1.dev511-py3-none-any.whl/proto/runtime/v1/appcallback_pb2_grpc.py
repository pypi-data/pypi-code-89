# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dapr.proto.common.v1 import common_pb2 as dapr_dot_proto_dot_common_dot_v1_dot_common__pb2
from dapr.proto.runtime.v1 import appcallback_pb2 as dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AppCallbackStub(object):
    """AppCallback V1 allows user application to interact with Dapr runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from dapr runtime.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OnInvoke = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/OnInvoke',
                request_serializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeResponse.FromString,
                )
        self.ListTopicSubscriptions = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/ListTopicSubscriptions',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListTopicSubscriptionsResponse.FromString,
                )
        self.OnTopicEvent = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/OnTopicEvent',
                request_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventResponse.FromString,
                )
        self.ListInputBindings = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/ListInputBindings',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListInputBindingsResponse.FromString,
                )
        self.OnBindingEvent = channel.unary_unary(
                '/dapr.proto.runtime.v1.AppCallback/OnBindingEvent',
                request_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventRequest.SerializeToString,
                response_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventResponse.FromString,
                )


class AppCallbackServicer(object):
    """AppCallback V1 allows user application to interact with Dapr runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from dapr runtime.
    """

    def OnInvoke(self, request, context):
        """Invokes service method with InvokeRequest.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTopicSubscriptions(self, request, context):
        """Lists all topics subscribed by this app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnTopicEvent(self, request, context):
        """Subscribes events from Pubsub
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInputBindings(self, request, context):
        """Lists all input bindings subscribed by this app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnBindingEvent(self, request, context):
        """Listens events from the input bindings

        User application can save the states or send the events to the output
        bindings optionally by returning BindingEventResponse.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppCallbackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OnInvoke': grpc.unary_unary_rpc_method_handler(
                    servicer.OnInvoke,
                    request_deserializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeResponse.SerializeToString,
            ),
            'ListTopicSubscriptions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTopicSubscriptions,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListTopicSubscriptionsResponse.SerializeToString,
            ),
            'OnTopicEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.OnTopicEvent,
                    request_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventResponse.SerializeToString,
            ),
            'ListInputBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListInputBindings,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListInputBindingsResponse.SerializeToString,
            ),
            'OnBindingEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.OnBindingEvent,
                    request_deserializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventRequest.FromString,
                    response_serializer=dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dapr.proto.runtime.v1.AppCallback', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppCallback(object):
    """AppCallback V1 allows user application to interact with Dapr runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from dapr runtime.
    """

    @staticmethod
    def OnInvoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dapr.proto.runtime.v1.AppCallback/OnInvoke',
            dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeRequest.SerializeToString,
            dapr_dot_proto_dot_common_dot_v1_dot_common__pb2.InvokeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTopicSubscriptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dapr.proto.runtime.v1.AppCallback/ListTopicSubscriptions',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListTopicSubscriptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnTopicEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dapr.proto.runtime.v1.AppCallback/OnTopicEvent',
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventRequest.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.TopicEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListInputBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dapr.proto.runtime.v1.AppCallback/ListInputBindings',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.ListInputBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnBindingEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dapr.proto.runtime.v1.AppCallback/OnBindingEvent',
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventRequest.SerializeToString,
            dapr_dot_proto_dot_runtime_dot_v1_dot_appcallback__pb2.BindingEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
