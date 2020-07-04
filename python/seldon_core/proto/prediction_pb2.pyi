# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.any_pb2 import (
    Any as google___protobuf___any_pb2___Any,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    ListValue as google___protobuf___struct_pb2___ListValue,
    Value as google___protobuf___struct_pb2___Value,
)

from tensorflow.core.framework.tensor_pb2 import (
    TensorProto as tensorflow___core___framework___tensor_pb2___TensorProto,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class SeldonMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    binData = ... # type: builtin___bytes
    strData = ... # type: typing___Text

    @property
    def status(self) -> global___Status: ...

    @property
    def meta(self) -> global___Meta: ...

    @property
    def data(self) -> global___DefaultData: ...

    @property
    def jsonData(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def customData(self) -> google___protobuf___any_pb2___Any: ...

    def __init__(self,
        *,
        status : typing___Optional[global___Status] = None,
        meta : typing___Optional[global___Meta] = None,
        data : typing___Optional[global___DefaultData] = None,
        binData : typing___Optional[builtin___bytes] = None,
        strData : typing___Optional[typing___Text] = None,
        jsonData : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        customData : typing___Optional[google___protobuf___any_pb2___Any] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SeldonMessage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"binData",b"binData",u"customData",b"customData",u"data",b"data",u"data_oneof",b"data_oneof",u"jsonData",b"jsonData",u"meta",b"meta",u"status",b"status",u"strData",b"strData"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"binData",b"binData",u"customData",b"customData",u"data",b"data",u"data_oneof",b"data_oneof",u"jsonData",b"jsonData",u"meta",b"meta",u"status",b"status",u"strData",b"strData"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"data_oneof",b"data_oneof"]) -> typing_extensions___Literal["data","binData","strData","jsonData","customData"]: ...
global___SeldonMessage = SeldonMessage

class DefaultData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    names = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def tensor(self) -> global___Tensor: ...

    @property
    def ndarray(self) -> google___protobuf___struct_pb2___ListValue: ...

    @property
    def tftensor(self) -> tensorflow___core___framework___tensor_pb2___TensorProto: ...

    def __init__(self,
        *,
        names : typing___Optional[typing___Iterable[typing___Text]] = None,
        tensor : typing___Optional[global___Tensor] = None,
        ndarray : typing___Optional[google___protobuf___struct_pb2___ListValue] = None,
        tftensor : typing___Optional[tensorflow___core___framework___tensor_pb2___TensorProto] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DefaultData: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DefaultData: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data_oneof",b"data_oneof",u"ndarray",b"ndarray",u"tensor",b"tensor",u"tftensor",b"tftensor"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data_oneof",b"data_oneof",u"names",b"names",u"ndarray",b"ndarray",u"tensor",b"tensor",u"tftensor",b"tftensor"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"data_oneof",b"data_oneof"]) -> typing_extensions___Literal["tensor","ndarray","tftensor"]: ...
global___DefaultData = DefaultData

class Tensor(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    shape = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int]
    values = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float]

    def __init__(self,
        *,
        shape : typing___Optional[typing___Iterable[builtin___int]] = None,
        values : typing___Optional[typing___Iterable[builtin___float]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Tensor: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tensor: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"shape",b"shape",u"values",b"values"]) -> None: ...
global___Tensor = Tensor

class Meta(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> google___protobuf___struct_pb2___Value: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Meta.TagsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Meta.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    global___TagsEntry = TagsEntry

    class RoutingEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: builtin___int

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Meta.RoutingEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Meta.RoutingEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    global___RoutingEntry = RoutingEntry

    class RequestPathEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Meta.RequestPathEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Meta.RequestPathEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    global___RequestPathEntry = RequestPathEntry

    puid = ... # type: typing___Text

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, google___protobuf___struct_pb2___Value]: ...

    @property
    def routing(self) -> typing___MutableMapping[typing___Text, builtin___int]: ...

    @property
    def requestPath(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    @property
    def metrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___Metric]: ...

    def __init__(self,
        *,
        puid : typing___Optional[typing___Text] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, google___protobuf___struct_pb2___Value]] = None,
        routing : typing___Optional[typing___Mapping[typing___Text, builtin___int]] = None,
        requestPath : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        metrics : typing___Optional[typing___Iterable[global___Metric]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Meta: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Meta: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"metrics",b"metrics",u"puid",b"puid",u"requestPath",b"requestPath",u"routing",b"routing",u"tags",b"tags"]) -> None: ...
global___Meta = Meta

class Metric(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MetricType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'Metric.MetricType': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['Metric.MetricType']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'Metric.MetricType']]: ...
        COUNTER = typing___cast('Metric.MetricType', 0)
        GAUGE = typing___cast('Metric.MetricType', 1)
        TIMER = typing___cast('Metric.MetricType', 2)
    COUNTER = typing___cast('Metric.MetricType', 0)
    GAUGE = typing___cast('Metric.MetricType', 1)
    TIMER = typing___cast('Metric.MetricType', 2)
    global___MetricType = MetricType

    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Metric.TagsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Metric.TagsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    global___TagsEntry = TagsEntry

    key = ... # type: typing___Text
    type = ... # type: global___Metric.MetricType
    value = ... # type: builtin___float

    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        key : typing___Optional[typing___Text] = None,
        type : typing___Optional[global___Metric.MetricType] = None,
        value : typing___Optional[builtin___float] = None,
        tags : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Metric: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Metric: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"tags",b"tags",u"type",b"type",u"value",b"value"]) -> None: ...
global___Metric = Metric

class SeldonMessageList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def seldonMessages(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SeldonMessage]: ...

    def __init__(self,
        *,
        seldonMessages : typing___Optional[typing___Iterable[global___SeldonMessage]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SeldonMessageList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonMessageList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"seldonMessages",b"seldonMessages"]) -> None: ...
global___SeldonMessageList = SeldonMessageList

class Status(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StatusFlag(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'Status.StatusFlag': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['Status.StatusFlag']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'Status.StatusFlag']]: ...
        SUCCESS = typing___cast('Status.StatusFlag', 0)
        FAILURE = typing___cast('Status.StatusFlag', 1)
    SUCCESS = typing___cast('Status.StatusFlag', 0)
    FAILURE = typing___cast('Status.StatusFlag', 1)
    global___StatusFlag = StatusFlag

    code = ... # type: builtin___int
    info = ... # type: typing___Text
    reason = ... # type: typing___Text
    status = ... # type: global___Status.StatusFlag

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        info : typing___Optional[typing___Text] = None,
        reason : typing___Optional[typing___Text] = None,
        status : typing___Optional[global___Status.StatusFlag] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Status: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Status: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"info",b"info",u"reason",b"reason",u"status",b"status"]) -> None: ...
global___Status = Status

class Feedback(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    reward = ... # type: builtin___float

    @property
    def request(self) -> global___SeldonMessage: ...

    @property
    def response(self) -> global___SeldonMessage: ...

    @property
    def truth(self) -> global___SeldonMessage: ...

    def __init__(self,
        *,
        request : typing___Optional[global___SeldonMessage] = None,
        response : typing___Optional[global___SeldonMessage] = None,
        reward : typing___Optional[builtin___float] = None,
        truth : typing___Optional[global___SeldonMessage] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Feedback: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Feedback: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"request",b"request",u"response",b"response",u"truth",b"truth"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request",b"request",u"response",b"response",u"reward",b"reward",u"truth",b"truth"]) -> None: ...
global___Feedback = Feedback

class RequestResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def request(self) -> global___SeldonMessage: ...

    @property
    def response(self) -> global___SeldonMessage: ...

    def __init__(self,
        *,
        request : typing___Optional[global___SeldonMessage] = None,
        response : typing___Optional[global___SeldonMessage] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RequestResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RequestResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"request",b"request",u"response",b"response"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"request",b"request",u"response",b"response"]) -> None: ...
global___RequestResponse = RequestResponse

class SeldonModelMetadataRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SeldonModelMetadataRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonModelMetadataRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...
global___SeldonModelMetadataRequest = SeldonModelMetadataRequest

class SeldonMessageMetadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    messagetype = ... # type: typing___Text
    name = ... # type: typing___Text
    datatype = ... # type: typing___Text
    shape = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int]

    @property
    def schema(self) -> google___protobuf___struct_pb2___Value: ...

    def __init__(self,
        *,
        messagetype : typing___Optional[typing___Text] = None,
        schema : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        name : typing___Optional[typing___Text] = None,
        datatype : typing___Optional[typing___Text] = None,
        shape : typing___Optional[typing___Iterable[builtin___int]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SeldonMessageMetadata: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonMessageMetadata: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"schema",b"schema"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"datatype",b"datatype",u"messagetype",b"messagetype",u"name",b"name",u"schema",b"schema",u"shape",b"shape"]) -> None: ...
global___SeldonMessageMetadata = SeldonMessageMetadata

class SeldonModelMetadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    versions = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    platform = ... # type: typing___Text

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SeldonMessageMetadata]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SeldonMessageMetadata]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        versions : typing___Optional[typing___Iterable[typing___Text]] = None,
        platform : typing___Optional[typing___Text] = None,
        inputs : typing___Optional[typing___Iterable[global___SeldonMessageMetadata]] = None,
        outputs : typing___Optional[typing___Iterable[global___SeldonMessageMetadata]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SeldonModelMetadata: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonModelMetadata: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"inputs",b"inputs",u"name",b"name",u"outputs",b"outputs",u"platform",b"platform",u"versions",b"versions"]) -> None: ...
global___SeldonModelMetadata = SeldonModelMetadata

class SeldonGraphMetadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ModelsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> global___SeldonModelMetadata: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[global___SeldonModelMetadata] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> SeldonGraphMetadata.ModelsEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonGraphMetadata.ModelsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    global___ModelsEntry = ModelsEntry

    name = ... # type: typing___Text

    @property
    def models(self) -> typing___MutableMapping[typing___Text, global___SeldonModelMetadata]: ...

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SeldonMessageMetadata]: ...

    @property
    def outputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___SeldonMessageMetadata]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        models : typing___Optional[typing___Mapping[typing___Text, global___SeldonModelMetadata]] = None,
        inputs : typing___Optional[typing___Iterable[global___SeldonMessageMetadata]] = None,
        outputs : typing___Optional[typing___Iterable[global___SeldonMessageMetadata]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SeldonGraphMetadata: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SeldonGraphMetadata: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"inputs",b"inputs",u"models",b"models",u"name",b"name",u"outputs",b"outputs"]) -> None: ...
global___SeldonGraphMetadata = SeldonGraphMetadata
