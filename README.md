# Ez Xml

`ez-xml` (easy xml) is a Python library that provides a simple way to generate XML representations of objects using the `lxml` library. It offers a base class `EzXMLModel` that can be inherited by your custom classes to easily convert them into XML.


# Usage
To use `ez-xml`, you need to create classes that inherit from EzXMLModel and define their own attributes. The library will automatically generate XML representations for the objects based on their attribute values.

Here's an example of how to use `ez-xml`:

```
import dataclasses
from lxml import etree
from ez.xml import EzXMLModel

@dataclasses.dataclass(frozen=True)
class Address(EzXMLModel):
    country: str

@dataclasses.dataclass(frozen=True)
class Seller(EzXMLModel):
    name: str
    address: Address

def main():
    seller = Seller("John Doe", Address("USA"))
    xml = seller.build()
    print(etree.tostring(xml, encoding="unicode"))
    >>> '<Seller><name>John Doe</name><Address><country>USA</country></Address></Seller>'
```