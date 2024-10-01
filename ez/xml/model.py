from lxml.builder import ElementMaker
import dataclasses
from typing import Any
from typing import Optional
from types import NoneType, UnionType
from typing import get_args, get_origin


def nsmap(nsmap):
    def decorator(cls):
        # Inject nsmap as an attribute when the class is instantiated
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.nsmap = nsmap  # Inject nsmap into the instance

        cls.__init__ = new_init
        return cls

    return decorator


@dataclasses.dataclass()
class EzXMLModel:
    def build(self, nsmap: dict | None = None) -> str:
        nsmap = nsmap or self.nsmap
        E = ElementMaker(nsmap=nsmap)

        children = []

        attributes = {}

        for field in dataclasses.fields(self):
            value = getattr(self, field.name)

            if value is None:
                continue

            field_type = _cleanup_field_type(field.type)

            if issubclass(field_type, EzXMLModel):
                children.append(value.build(nsmap))
            elif field.name == "value":
                children.append(str(value))
            elif field.metadata and field.metadata.get("_type", None) == "attribute":
                attributes[field.name] = str(value)
            else:
                sub_ns = field.metadata.get("_ns", None) if field.metadata else None
                sub_ns = "{" + nsmap.get(sub_ns) + "}" if sub_ns else ""
                children.append(getattr(E, sub_ns + field.name)(str(value)))

            _ns = getattr(self, "_ns", None)

            _ns = "{" + nsmap.get(_ns) + "}" if _ns else ""

        return getattr(E, _ns + type(self).__name__)(*children, **attributes)


def _cleanup_field_type(field_type: Any):
    if not type(field_type) == UnionType:
        return field_type

    type_list = list(get_args(field_type))
    if NoneType in type_list:
        type_list.remove(NoneType)
    # TODO: raise exception if more than 1 types

    return type_list[0]


def EzField(ns: str | None = None, type: str | None = None, **kwargs: Any):
    metadata = {}
    if ns:
        metadata["_ns"] = ns
    if type:
        metadata["_type"] = type
    return dataclasses.field(metadata=metadata, **kwargs)
