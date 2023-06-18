from lxml.builder import ElementMaker


class EzXMLModel:
    def build(self) -> str:
        E = ElementMaker()

        children = []

        for name, value in self.__dict__.items():
            if isinstance(value, EzXMLModel):
                children.append(value.build())
            else:
                children.append(getattr(E, name)(str(value)))

        return getattr(E, type(self).__name__)(*children)
