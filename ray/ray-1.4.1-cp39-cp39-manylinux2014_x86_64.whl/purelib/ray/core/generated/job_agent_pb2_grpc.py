# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import job_agent_pb2 as src_dot_ray_dot_protobuf_dot_job__agent__pb2


class JobAgentServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InitializeJobEnv = channel.unary_unary(
        '/ray.rpc.JobAgentService/InitializeJobEnv',
        request_serializer=src_dot_ray_dot_protobuf_dot_job__agent__pb2.InitializeJobEnvRequest.SerializeToString,
        response_deserializer=src_dot_ray_dot_protobuf_dot_job__agent__pb2.InitializeJobEnvReply.FromString,
        )


class JobAgentServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def InitializeJobEnv(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobAgentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InitializeJobEnv': grpc.unary_unary_rpc_method_handler(
          servicer.InitializeJobEnv,
          request_deserializer=src_dot_ray_dot_protobuf_dot_job__agent__pb2.InitializeJobEnvRequest.FromString,
          response_serializer=src_dot_ray_dot_protobuf_dot_job__agent__pb2.InitializeJobEnvReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ray.rpc.JobAgentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
