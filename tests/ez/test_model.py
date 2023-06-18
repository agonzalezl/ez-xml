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


def test_dummy():
    thing = Seller("John Doe", Address("USA")).build()
    assert (
        etree.tostring(thing, encoding="unicode") == "<Seller"
        "><name>John Doe</name>"
        "<Address><country>USA</country></Address>"
        "</Seller>"
    )
