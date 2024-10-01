from lxml.builder import ElementMaker
import dataclasses


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

            if issubclass(field.type, EzXMLModel):
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


def EzField(ns: str | None = None, type: str | None = None):
    metadata = {}
    if ns:
        metadata["_ns"] = ns
    if type:
        metadata["_type"] = type
    return dataclasses.field(metadata=metadata)
