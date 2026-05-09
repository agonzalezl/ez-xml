from lxml import etree

from ez.xml.model_pydantic import EzField, PydanticEzXMLModel


class Province(PydanticEzXMLModel):
    _ns = "cdc"
    _nsmap = {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    value: str
    code: str = EzField(type="attribute")


class Address(PydanticEzXMLModel):
    _ns = "cdc"
    _nsmap = {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    Country: str = EzField(ns="xsi")
    province: Province


class Balance(PydanticEzXMLModel):
    _ns = "cdc"
    _nsmap = {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    value: str
    currency: str = EzField(type="attribute")


class LineItem(PydanticEzXMLModel):
    _ns = "cdc"
    _nsmap = {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    SKU: str = EzField("cdc")


class Order(PydanticEzXMLModel):
    _ns = "cdc"
    _nsmap = {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    lines: list[LineItem] = []


def test_list_of_models():
    thing = Order(lines=[LineItem(SKU="A1"), LineItem(SKU="B2")]).build()

    assert (
        etree.tostring(thing, encoding="unicode")
        == '<cdc:Order xmlns:cdc="http://www.cdc.com/schema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<cdc:LineItem><cdc:SKU>A1</cdc:SKU></cdc:LineItem>"
        "<cdc:LineItem><cdc:SKU>B2</cdc:SKU></cdc:LineItem>"
        "</cdc:Order>"
    )


class Seller(PydanticEzXMLModel):
    _ns = "cdc"
    _nsmap = {
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    Name: str = EzField(ns="xsi")
    address: Address
    balance: Balance


def test_model():
    thing = Seller(
        Name="John Doe",
        address=Address(Country="USA", province=Province(value="New York", code="NY")),
        balance=Balance(value="33", currency="EUR"),
    ).build()

    assert (
        etree.tostring(thing, encoding="unicode")
        == '<cdc:Seller xmlns:cdc="http://www.cdc.com/schema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<xsi:Name>John Doe</xsi:Name>"
        "<cdc:Address>"
        "<xsi:Country>USA</xsi:Country>"
        '<cdc:Province code="NY">New York</cdc:Province>'
        "</cdc:Address>"
        '<cdc:Balance currency="EUR">33</cdc:Balance>'
        "</cdc:Seller>"
    )


class SellerOptional(PydanticEzXMLModel):
    _ns = None
    _nsmap = {
        None: "http://optional.namespace.com/",
        "cdc": "http://www.cdc.com/schema",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    Name: str = EzField(ns="xsi")
    address: Address | None = None
    balance: Balance | None = None


def test_optional():
    thing = SellerOptional(
        Name="John Doe",
        balance=Balance(value="33", currency="EUR"),
    ).build()

    assert (
        etree.tostring(thing, encoding="unicode")
        == '<SellerOptional xmlns="http://optional.namespace.com/" xmlns:cdc="http://www.cdc.com/schema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<xsi:Name>John Doe</xsi:Name>"
        '<cdc:Balance currency="EUR">33</cdc:Balance>'
        "</SellerOptional>"
    )
