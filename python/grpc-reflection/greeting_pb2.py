# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egreeting.proto\x12\nhelloworld\"\x07\n\x05\x45mpty\" \n\rGreetingReply\x12\x0f\n\x07message\x18\x01 \x01(\t2E\n\x07Greeter\x12:\n\x08Greeting\x12\x11.helloworld.Empty\x1a\x19.helloworld.GreetingReply\"\x00\x62\x06proto3')



_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_GREETINGREPLY = DESCRIPTOR.message_types_by_name['GreetingReply']
Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'greeting_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Empty)
  })
_sym_db.RegisterMessage(Empty)

GreetingReply = _reflection.GeneratedProtocolMessageType('GreetingReply', (_message.Message,), {
  'DESCRIPTOR' : _GREETINGREPLY,
  '__module__' : 'greeting_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.GreetingReply)
  })
_sym_db.RegisterMessage(GreetingReply)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=30
  _EMPTY._serialized_end=37
  _GREETINGREPLY._serialized_start=39
  _GREETINGREPLY._serialized_end=71
  _GREETER._serialized_start=73
  _GREETER._serialized_end=142
# @@protoc_insertion_point(module_scope)
