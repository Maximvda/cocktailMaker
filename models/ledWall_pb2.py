# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ledWall.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ledWall.proto',
  package='ledwall',
  syntax='proto3',
  serialized_pb=_b('\n\rledWall.proto\x12\x07ledwall\"\x83\x01\n\x07Upgrade\x12\x12\n\ndeviceType\x18\x01 \x01(\r\x12\x11\n\timageSize\x18\x02 \x01(\r\x12\x1c\n\x14\x66irmWareMajorVersion\x18\x03 \x01(\r\x12\x1c\n\x14\x66irmWareMinorVersion\x18\x04 \x01(\r\x12\x15\n\rserialNumbers\x18\x05 \x03(\r\"m\n\x08\x43ocktail\x12\x10\n\x08\x63ocktail\x18\x01 \x01(\r\x12\x10\n\x08\x61maretto\x18\x02 \x01(\r\x12\x0c\n\x04lime\x18\x03 \x01(\r\x12\x0e\n\x06\x62randy\x18\x04 \x01(\r\x12\x0b\n\x03rum\x18\x05 \x01(\r\x12\x12\n\ntriple_sec\x18\x06 \x01(\r\"[\n\x07LedMode\x12\r\n\x05\x63olor\x18\x01 \x01(\r\x12\x0c\n\x04mode\x18\x02 \x01(\r\x12\t\n\x01R\x18\x03 \x01(\r\x12\t\n\x01G\x18\x04 \x01(\r\x12\t\n\x01\x42\x18\x05 \x01(\r\x12\x12\n\nbrightness\x18\x06 \x01(\r\"\x85\x01\n\x07\x43ommand\x12#\n\x07upgrade\x18\x01 \x01(\x0b\x32\x10.ledwall.UpgradeH\x00\x12%\n\x08\x63ocktail\x18\x02 \x01(\x0b\x32\x11.ledwall.CocktailH\x00\x12#\n\x07ledmode\x18\x03 \x01(\x0b\x32\x10.ledwall.LedModeH\x00\x42\t\n\x07\x63ommand\".\n\x08\x43ommands\x12\"\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x10.ledwall.Commandb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UPGRADE = _descriptor.Descriptor(
  name='Upgrade',
  full_name='ledwall.Upgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceType', full_name='ledwall.Upgrade.deviceType', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageSize', full_name='ledwall.Upgrade.imageSize', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmWareMajorVersion', full_name='ledwall.Upgrade.firmWareMajorVersion', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmWareMinorVersion', full_name='ledwall.Upgrade.firmWareMinorVersion', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialNumbers', full_name='ledwall.Upgrade.serialNumbers', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=158,
)


_COCKTAIL = _descriptor.Descriptor(
  name='Cocktail',
  full_name='ledwall.Cocktail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cocktail', full_name='ledwall.Cocktail.cocktail', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amaretto', full_name='ledwall.Cocktail.amaretto', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lime', full_name='ledwall.Cocktail.lime', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brandy', full_name='ledwall.Cocktail.brandy', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rum', full_name='ledwall.Cocktail.rum', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='triple_sec', full_name='ledwall.Cocktail.triple_sec', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=269,
)


_LEDMODE = _descriptor.Descriptor(
  name='LedMode',
  full_name='ledwall.LedMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='ledwall.LedMode.color', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='ledwall.LedMode.mode', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='R', full_name='ledwall.LedMode.R', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='G', full_name='ledwall.LedMode.G', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='B', full_name='ledwall.LedMode.B', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brightness', full_name='ledwall.LedMode.brightness', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=362,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='ledwall.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='ledwall.Command.upgrade', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cocktail', full_name='ledwall.Command.cocktail', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ledmode', full_name='ledwall.Command.ledmode', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='command', full_name='ledwall.Command.command',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=365,
  serialized_end=498,
)


_COMMANDS = _descriptor.Descriptor(
  name='Commands',
  full_name='ledwall.Commands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='ledwall.Commands.commands', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=546,
)

_COMMAND.fields_by_name['upgrade'].message_type = _UPGRADE
_COMMAND.fields_by_name['cocktail'].message_type = _COCKTAIL
_COMMAND.fields_by_name['ledmode'].message_type = _LEDMODE
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['upgrade'])
_COMMAND.fields_by_name['upgrade'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['cocktail'])
_COMMAND.fields_by_name['cocktail'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMAND.oneofs_by_name['command'].fields.append(
  _COMMAND.fields_by_name['ledmode'])
_COMMAND.fields_by_name['ledmode'].containing_oneof = _COMMAND.oneofs_by_name['command']
_COMMANDS.fields_by_name['commands'].message_type = _COMMAND
DESCRIPTOR.message_types_by_name['Upgrade'] = _UPGRADE
DESCRIPTOR.message_types_by_name['Cocktail'] = _COCKTAIL
DESCRIPTOR.message_types_by_name['LedMode'] = _LEDMODE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Commands'] = _COMMANDS

Upgrade = _reflection.GeneratedProtocolMessageType('Upgrade', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADE,
  __module__ = 'ledWall_pb2'
  # @@protoc_insertion_point(class_scope:ledwall.Upgrade)
  ))
_sym_db.RegisterMessage(Upgrade)

Cocktail = _reflection.GeneratedProtocolMessageType('Cocktail', (_message.Message,), dict(
  DESCRIPTOR = _COCKTAIL,
  __module__ = 'ledWall_pb2'
  # @@protoc_insertion_point(class_scope:ledwall.Cocktail)
  ))
_sym_db.RegisterMessage(Cocktail)

LedMode = _reflection.GeneratedProtocolMessageType('LedMode', (_message.Message,), dict(
  DESCRIPTOR = _LEDMODE,
  __module__ = 'ledWall_pb2'
  # @@protoc_insertion_point(class_scope:ledwall.LedMode)
  ))
_sym_db.RegisterMessage(LedMode)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'ledWall_pb2'
  # @@protoc_insertion_point(class_scope:ledwall.Command)
  ))
_sym_db.RegisterMessage(Command)

Commands = _reflection.GeneratedProtocolMessageType('Commands', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDS,
  __module__ = 'ledWall_pb2'
  # @@protoc_insertion_point(class_scope:ledwall.Commands)
  ))
_sym_db.RegisterMessage(Commands)


# @@protoc_insertion_point(module_scope)
