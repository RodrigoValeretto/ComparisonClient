from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CompareRQ(_message.Message):
    __slots__ = ["GUID", "image"]
    GUID: str
    GUID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    def __init__(self, image: _Optional[bytes] = ..., GUID: _Optional[str] = ...) -> None: ...

class CompareRS(_message.Message):
    __slots__ = ["isEqual"]
    ISEQUAL_FIELD_NUMBER: _ClassVar[int]
    isEqual: bool
    def __init__(self, isEqual: bool = ...) -> None: ...
