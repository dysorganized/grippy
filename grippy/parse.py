import inspect
from typing import Tuple

from grippy.proto_message import ProtoField, ProtoMessage


def parse_rpc(rpc: callable) -> Tuple[ProtoMessage, ProtoMessage]:
    annotations = inspect.get_annotations(rpc)
    return_message = ProtoMessage(
        name=f"{rpc.__name__}Return",
        fields=[
            ProtoField(name="return", type=annotations.pop("return"), num=1)
        ]
    )
    request_message = ProtoMessage(
        name=f"{rpc.__name__}Request", fields=[
            ProtoField(name=name, type=type, num=i)
            for i, (name, type) in enumerate(annotations.items(), start=1)
        ]
    )
    return request_message, return_message
