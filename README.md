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


# UBL 2.1 Support

`ez-xml` includes pre-built support for the [OASIS UBL 2.1](https://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html) invoice specification. The `ez.ubl` module provides ready-to-use classes for generating UBL Invoice documents.

## Example

```python
from ez.ubl import (
    Invoice, InvoiceLine, OrderReference, AccountingSupplierParty,
    AccountingCustomerParty, LegalMonetaryTotal, Party, PartyName,
    PayableAmount, LineExtensionAmount, Item, TaxTotal, TaxSubtotal,
    TaxCategory, TaxScheme, TaxAmount
)

invoice = Invoice(
    ID="INV-001",
    IssueDate="2024-01-15",
    AccountingSupplierParty=AccountingSupplierParty(
        Party=Party(PartyName=PartyName(Name="ACME Corp"))
    ),
    AccountingCustomerParty=AccountingCustomerParty(
        Party=Party(PartyName=PartyName(Name="Client Inc"))
    ),
    TaxTotal=[
        TaxTotal(
            TaxAmount=TaxAmount(value="20.00", currencyID="EUR"),
            TaxSubtotal=[
                TaxSubtotal(
                    TaxableAmount=TaxAmount(value="100.00", currencyID="EUR"),
                    TaxAmount=TaxAmount(value="20.00", currencyID="EUR"),
                    TaxCategory=TaxCategory(
                        ID="S", Percent="20",
                        TaxScheme=TaxScheme(ID="VAT")
                    )
                )
            ]
        )
    ],
    LegalMonetaryTotal=LegalMonetaryTotal(
        PayableAmount=PayableAmount(value="120.00", currencyID="EUR")
    ),
    InvoiceLine=[
        InvoiceLine(
            ID="1",
            LineExtensionAmount=LineExtensionAmount(value="100.00", currencyID="EUR"),
            Item=Item(Description="Service A")
        )
    ],
)

xml = invoice.build()
```

The generated XML is fully compliant with the UBL 2.1 XSD schema and can be validated against the official OASIS specification.


# Peppol BIS 3.0 Support

`ez-xml` includes pre-built support for the [Peppol BIS Billing 3.0](https://peppol.eu) specification. The `ez.peppol` module provides ready-to-use classes for generating Peppol-compliant Invoice documents. These classes extend the UBL 2.1 support with Peppol-specific requirements such as mandatory `EndpointID`, `BuyerReference`, `ClassifiedTaxCategory` on items, and price-per-line details.

## Example

```python
from ez.peppol import (
    Invoice, InvoiceLine, AccountingSupplierParty, AccountingCustomerParty,
    Party, PartyName, PartyLegalEntity, PostalAddress, Country,
    LegalMonetaryTotal, PayableAmount, LineExtensionAmount,
    TaxExclusiveAmount, TaxInclusiveAmount, TaxTotal, TaxSubtotal,
    TaxCategory, TaxScheme, TaxAmount, TaxableAmount, Item, Price,
    PriceAmount, InvoicedQuantity, ClassifiedTaxCategory, EndpointID,
)

invoice = Invoice(
    ID="INV-001",
    IssueDate="2024-01-15",
    DueDate="2024-01-22",
    InvoiceTypeCode="380",
    DocumentCurrencyCode="EUR",
    BuyerReference="BUYER-REF-001",
    AccountingSupplierParty=AccountingSupplierParty(
        Party=Party(
            EndpointID=EndpointID("1548079098355", schemeID="0088"),
            PartyName=PartyName(Name="Seller Ltd"),
            PostalAddress=PostalAddress(
                Country=Country(IdentificationCode="GB")
            ),
            PartyLegalEntity=[PartyLegalEntity(RegistrationName="Seller LTD")],
        )
    ),
    AccountingCustomerParty=AccountingCustomerParty(
        Party=Party(
            EndpointID=EndpointID("1548079098355", schemeID="0088"),
            PartyName=PartyName(Name="Buyer Inc"),
            PostalAddress=PostalAddress(
                Country=Country(IdentificationCode="DE")
            ),
            PartyLegalEntity=[PartyLegalEntity(RegistrationName="Buyer INC")],
        )
    ),
    TaxTotal=[
        TaxTotal(
            TaxAmount=TaxAmount(value="20.00", currencyID="EUR"),
            TaxSubtotal=[
                TaxSubtotal(
                    TaxableAmount=TaxableAmount(value="100.00", currencyID="EUR"),
                    TaxAmount=TaxAmount(value="20.00", currencyID="EUR"),
                    TaxCategory=TaxCategory(
                        ID="S", Percent="20",
                        TaxScheme=TaxScheme(ID="VAT")
                    )
                )
            ]
        )
    ],
    LegalMonetaryTotal=LegalMonetaryTotal(
        LineExtensionAmount=LineExtensionAmount(value="100.00", currencyID="EUR"),
        TaxExclusiveAmount=TaxExclusiveAmount(value="100.00", currencyID="EUR"),
        TaxInclusiveAmount=TaxInclusiveAmount(value="120.00", currencyID="EUR"),
        PayableAmount=PayableAmount(value="120.00", currencyID="EUR"),
    ),
    InvoiceLines=[
        InvoiceLine(
            ID="1",
            InvoicedQuantity=InvoicedQuantity(value="1", unitCode="C62"),
            LineExtensionAmount=LineExtensionAmount(value="100.00", currencyID="EUR"),
            Item=Item(
                Name="Services",
                Description="Consulting services",
                ClassifiedTaxCategory=ClassifiedTaxCategory(ID="S", Percent="20"),
            ),
            Price=Price(PriceAmount=PriceAmount(value="100.00", currencyID="EUR")),
        )
    ],
)

xml = invoice.build()
```

The generated XML is fully compliant with the Peppol BIS 3.0 specification and can be validated against the official PEPPOL and CEN Schematron rules.


## Roadmap

- UBL 2.1 Document Support
  - CreditNote - Credit memo
  - Order - Purchase order
  - DespatchAdvice - Shipment notice

- Peppol BIS Support
  - Invoice - Update to Peppol BIS Billing 3.0
  - CreditNote - Peppol BIS CreditNote
  - Order - Peppol BIS Order

- XML Parsing
  - Implement parsing (XML → Python objects)
