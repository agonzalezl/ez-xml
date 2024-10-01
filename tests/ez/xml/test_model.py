import dataclasses

from lxml import etree

from ez.xml import EzXMLModel, nsmap, EzField


@dataclasses.dataclass()
class Province(EzXMLModel):
    _ns = "cdc"
    value: str
    code: str = EzField(type="attribute")


@dataclasses.dataclass()
class Address(EzXMLModel):
    _ns = "cdc"
    Country: str = dataclasses.field(metadata={"_ns": "xsi"})
    province: Province


@dataclasses.dataclass()
class Balance(EzXMLModel):
    _ns = "cdc"
    value: str
    currency: str = EzField(type="attribute")


@nsmap(
    {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
)
@dataclasses.dataclass()
class Seller(EzXMLModel):
    Name: str = EzField(ns="xsi")
    address: Address
    balance: Balance


def test_dummy():
    thing = Seller(
        Name="John Doe",
        address=Address(Country="USA", province=Province("New York", code="NY")),
        balance=Balance(value="33", currency="EUR"),
    ).build()

    assert (
        etree.tostring(thing, encoding="unicode")
        == '<Seller xmlns:cdc="http://www.cdc.com/schema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<xsi:Name>John Doe</xsi:Name>"
        "<cdc:Address>"
        "<xsi:Country>USA</xsi:Country>"
        '<cdc:Province code="NY">New York</cdc:Province>'
        "</cdc:Address>"
        '<cdc:Balance currency="EUR">33</cdc:Balance>'
        "</Seller>"
    )
