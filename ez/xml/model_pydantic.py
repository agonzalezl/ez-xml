from __future__ import annotations
from lxml.builder import ElementMaker
import lxml.etree
from typing import Any, ClassVar, get_args, get_origin
from types import UnionType
from pydantic import BaseModel, Field


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


def EzField(
    ns: str | None = None,
    type: str | None = None,
    **kwargs: Any,
):
    extra = {}
    if ns:
        extra["xml_ns"] = ns
    if type == "attribute":
        extra["xml_attribute"] = True
    if extra:
        kwargs["json_schema_extra"] = {**kwargs.get("json_schema_extra", {}), **extra}
    return Field(**kwargs)


class PydanticEzXMLModel(BaseModel):
    _ns: ClassVar[str | None] = None
    _nsmap: ClassVar[dict | None] = None

    model_config = {"arbitrary_types_allowed": True}

    def build(self, nsmap: dict | None = None) -> lxml.etree._Element:
        nsmap = nsmap or self._nsmap
        E = ElementMaker(nsmap=nsmap)

        children = []
        attributes = {}

        for field_name, field_info in type(self).model_fields.items():
            value = getattr(self, field_name)

            if value is None:
                continue

            field_type = field_info.annotation
            field_type = _cleanup_field_type(field_type)

            extra = field_info.json_schema_extra or {}
            xml_ns = extra.get("xml_ns")
            xml_attribute = extra.get("xml_attribute", False)

            if get_origin(field_type) is list:
                args = get_args(field_type)
                if args:
                    item_type = _cleanup_field_type(args[0])
                    if isinstance(item_type, type) and issubclass(
                        item_type, (PydanticEzXMLModel,)
                    ):
                        for item in value:
                            children.append(item.build(nsmap))
                        continue

            if isinstance(field_type, type) and issubclass(
                field_type, (PydanticEzXMLModel,)
            ):
                children.append(value.build(nsmap))
            elif field_name == "value":
                children.append(str(value))
            elif xml_attribute:
                attributes[field_name] = str(value)
            else:
                if ns := (nsmap or {}).get(xml_ns or ""):
                    prefix = "{" + ns + "}"
                else:
                    prefix = ""
                children.append(getattr(E, prefix + field_name)(str(value)))

        _ns_key = self._ns
        _ns = (nsmap or {}).get(_ns_key, None)
        _ns = "{" + _ns + "}" if _ns else ""
        return getattr(E, _ns + type(self).__name__)(*children, **attributes)
