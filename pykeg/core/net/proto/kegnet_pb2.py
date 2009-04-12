#!/usr/bin/python2.4
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2


_WIREMESSAGE_MESSAGEID = descriptor.EnumDescriptor(
  name='MessageId',
  full_name='WireMessage.MessageId',
  filename='MessageId',
  values=[
    descriptor.EnumValueDescriptor(
      name='RESERVED', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CLIENT_CONNECT', index=1, number=1000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CLIENT_DISCONNECT', index=2, number=1001,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_REPLY', index=3, number=1002,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PING_REQUEST', index=4, number=1003,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PING_REPLY', index=5, number=1004,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='REGISTER_FLOW_DEV', index=6, number=2001,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UNREGISTER_FLOW_DEV', index=7, number=2002,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FLOW_UPDATE', index=8, number=2003,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FLOW_END', index=9, number=2004,
      options=None,
      type=None),
  ],
  options=None,
)

_STATUSREPLY_STATUSCODE = descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='StatusReply.StatusCode',
  filename='StatusCode',
  values=[
    descriptor.EnumValueDescriptor(
      name='OK', index=0, number=200,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=400,
      options=None,
      type=None),
  ],
  options=None,
)


_WIREMESSAGE = descriptor.Descriptor(
  name='WireMessage',
  full_name='WireMessage',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message_length', full_name='WireMessage.message_length', index=0,
      number=1, type=7, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message_type', full_name='WireMessage.message_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='WireMessage.data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _WIREMESSAGE_MESSAGEID,
  ],
  options=None)


_CLIENTCONNECT = descriptor.Descriptor(
  name='ClientConnect',
  full_name='ClientConnect',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_name', full_name='ClientConnect.client_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_CLIENTDISCONNECT = descriptor.Descriptor(
  name='ClientDisconnect',
  full_name='ClientDisconnect',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_name', full_name='ClientDisconnect.client_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_STATUSREPLY = descriptor.Descriptor(
  name='StatusReply',
  full_name='StatusReply',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='StatusReply.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      default_value=200,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='StatusReply.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
    _STATUSREPLY_STATUSCODE,
  ],
  options=None)


_PINGREQUEST = descriptor.Descriptor(
  name='PingRequest',
  full_name='PingRequest',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='seqn', full_name='PingRequest.seqn', index=0,
      number=1, type=7, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_PINGREPLY = descriptor.Descriptor(
  name='PingReply',
  full_name='PingReply',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='seqn', full_name='PingReply.seqn', index=0,
      number=1, type=7, cpp_type=3, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_REGISTERFLOWDEV = descriptor.Descriptor(
  name='RegisterFlowDev',
  full_name='RegisterFlowDev',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='RegisterFlowDev.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_UNREGISTERFLOWDEV = descriptor.Descriptor(
  name='UnregisterFlowDev',
  full_name='UnregisterFlowDev',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='UnregisterFlowDev.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FLOWUPDATE = descriptor.Descriptor(
  name='FlowUpdate',
  full_name='FlowUpdate',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='FlowUpdate.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='FlowUpdate.count', index=1,
      number=2, type=13, cpp_type=3, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_FLOWEND = descriptor.Descriptor(
  name='FlowEnd',
  full_name='FlowEnd',
  filename='kegnet.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='FlowEnd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_WIREMESSAGE.fields_by_name['message_type'].enum_type = _WIREMESSAGE_MESSAGEID
_STATUSREPLY.fields_by_name['code'].enum_type = _STATUSREPLY_STATUSCODE

class WireMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WIREMESSAGE

class ClientConnect(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLIENTCONNECT

class ClientDisconnect(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLIENTDISCONNECT

class StatusReply(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATUSREPLY

class PingRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGREQUEST

class PingReply(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PINGREPLY

class RegisterFlowDev(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERFLOWDEV

class UnregisterFlowDev(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNREGISTERFLOWDEV

class FlowUpdate(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FLOWUPDATE

class FlowEnd(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FLOWEND

