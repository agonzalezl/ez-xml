from __future__ import annotations
from lxml.builder import ElementMaker
import dataclasses
from typing import Any, ClassVar, get_args, get_origin, get_type_hints, Union
from types import UnionType
import lxml.etree


def nsmap(nsmap):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.nsmap = nsmap

        cls.__init__ = new_init
        return cls

    return decorator


@dataclasses.dataclass()
class EzXMLModel:
    nsmap: ClassVar[dict | None] = None

    def build(self, nsmap: dict | None = None) -> lxml.etree._Element:
        nsmap = nsmap or self.nsmap
        E = ElementMaker(nsmap=nsmap)

        children = []

        attributes = {}

        hints = get_type_hints(self.__class__)

        for field in dataclasses.fields(self):
            value = getattr(self, field.name)

            if value is None:
                continue

            field_type = hints.get(field.name, field.type)
            field_type = _cleanup_field_type(field_type)

            if get_origin(field_type) is list:
                args = get_args(field_type)
                if args:
                    item_type = _cleanup_field_type(args[0])
                    if isinstance(item_type, type) and issubclass(
                        item_type, EzXMLModel
                    ):
                        for item in value:
                            children.append(item.build(nsmap))
                        continue

            if isinstance(field_type, type) and issubclass(field_type, EzXMLModel):
                children.append(value.build(nsmap))
            elif field.name == "value":
                children.append(str(value))
            elif field.metadata and field.metadata.get("_type", None) == "attribute":
                attributes[field.name] = str(value)
            else:
                sub_ns = field.metadata.get("_ns", None) if field.metadata else None
                if ns := (nsmap or {}).get(sub_ns):
                    sub_ns = "{" + ns + "}"
                else:
                    sub_ns = ""
                children.append(getattr(E, sub_ns + field.name)(str(value)))

        _ns_key = getattr(self, "_ns", None)
        _ns = (nsmap or {}).get(_ns_key, None)
        _ns = "{" + _ns + "}" if _ns else ""

        return getattr(E, _ns + type(self).__name__)(*children, **attributes)


def _cleanup_field_type(field_type: Any):
    if isinstance(field_type, str):
        return field_type
    if not isinstance(field_type, UnionType):
        return field_type

    type_list = list(get_args(field_type))
    if None in type_list:
        type_list.remove(None)
    if len(type_list) == 1:
        return type_list[0]
    if len(type_list) > 1:
        return type_list[0]
    return field_type


def EzField(ns: str | None = None, type: str | None = None, **kwargs: Any):
    metadata = {}
    if ns:
        metadata["_ns"] = ns
    if type:
        metadata["_type"] = type
    return dataclasses.field(metadata=metadata, **kwargs)
