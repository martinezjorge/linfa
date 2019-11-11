# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14protos/service.proto\"\"\n\x0ePredictRequest\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x03(\x01\"(\n\x0fPredictResponse\x12\x15\n\rcluster_index\x18\x01 \x01(\r2A\n\x11\x43lusteringService\x12,\n\x07Predict\x12\x0f.PredictRequest\x1a\x10.PredictResponseb\x06proto3')
)




_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='PredictRequest.features', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=58,
)


_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_index', full_name='PredictResponse.cluster_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'protos.service_pb2'
  # @@protoc_insertion_point(class_scope:PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'protos.service_pb2'
  # @@protoc_insertion_point(class_scope:PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)



_CLUSTERINGSERVICE = _descriptor.ServiceDescriptor(
  name='ClusteringService',
  full_name='ClusteringService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=102,
  serialized_end=167,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='ClusteringService.Predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_PREDICTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLUSTERINGSERVICE)

DESCRIPTOR.services_by_name['ClusteringService'] = _CLUSTERINGSERVICE

# @@protoc_insertion_point(module_scope)
