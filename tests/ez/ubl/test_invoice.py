from ez.ubl._invoice import (
    Invoice,
    InvoiceLine,
    OrderReference,
    AccountingSupplierParty,
    AccountingCustomerParty,
    LegalMonetaryTotal,
    Party,
    PartyName,
    PayableAmount,
    LineExtensionAmount,
    Item,
    TaxTotal,
    TaxSubtotal,
    TaxCategory,
    TaxScheme,
    TaxAmount,
    TaxableAmount,
    PartyIdentification,
    Contact,
    Address,
    Country,
    Delivery,
    DeliveryTerms,
    PaymentMeans,
    PaymentTerms,
    PrepaidPayment,
    AllowanceCharge,
    DocumentReference,
    BillingReference,
    ProjectReference,
    InvoicePeriod,
    Signature,
    PayeeParty,
    BuyerCustomerParty,
    SellerSupplierParty,
    TaxRepresentativeParty,
    TaxExchangeRate,
)
from lxml import etree
from pathlib import Path


def test_invoice_build():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        InvoiceTypeCode="1",
        Note="Note",
        DocumentCurrencyCode="eur",
        OrderReference=OrderReference(
            ID="1111111111",
            SalesOrderID="aaaaaaaaa",
            UUID="2222222",
            IssueDate="2017-12-01",
        ),
        AccountingSupplierParty=AccountingSupplierParty(
            Party=Party(PartyName=PartyName(Name="Seller Co"))
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(PartyName=PartyName(Name="Buyer Co"))
        ),
        TaxTotal=[
            TaxTotal(
                TaxAmount=TaxAmount(value="20.00", currencyID="EUR"),
                TaxSubtotal=[
                    TaxSubtotal(
                        TaxableAmount=TaxableAmount(value="100.00", currencyID="EUR"),
                        TaxAmount=TaxAmount(value="20.00", currencyID="EUR"),
                        TaxCategory=TaxCategory(
                            ID="S", Percent="20", TaxScheme=TaxScheme(ID="VAT")
                        ),
                    )
                ],
            )
        ],
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="120.00", currencyID="EUR")
        ),
        invoiceLine=[
            InvoiceLine(
                ID="123",
                LineExtensionAmount=LineExtensionAmount(
                    value="50.00", currencyID="EUR"
                ),
                Item=Item(Description="Service A"),
            ),
            InvoiceLine(
                ID="456",
                LineExtensionAmount=LineExtensionAmount(
                    value="50.00", currencyID="EUR"
                ),
                Item=Item(Description="Service B"),
            ),
        ],
    ).build()

    xml = etree.tostring(invoice, encoding="unicode")

    assert xml.startswith(
        '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"'
    )
    assert "<cbc:ID>12345</cbc:ID>" in xml
    assert "<cbc:IssueDate>2017-12-01</cbc:IssueDate>" in xml
    assert "<cbc:InvoiceTypeCode>1</cbc:InvoiceTypeCode>" in xml
    assert "<cbc:Note>Note</cbc:Note>" in xml
    assert "<cbc:DocumentCurrencyCode>eur</cbc:DocumentCurrencyCode>" in xml
    assert "<cac:OrderReference>" in xml
    assert "<cac:AccountingSupplierParty>" in xml
    assert "<cac:AccountingCustomerParty>" in xml
    assert "<cac:TaxTotal>" in xml
    assert "<cac:TaxSubtotal>" in xml
    assert "<cac:TaxCategory>" in xml
    assert "<cac:TaxScheme>" in xml
    assert '<cbc:TaxAmount currencyID="EUR">20.00</cbc:TaxAmount>' in xml
    assert "<cac:LegalMonetaryTotal>" in xml
    assert '<cbc:PayableAmount currencyID="EUR">120.00</cbc:PayableAmount>' in xml
    assert "<cac:InvoiceLine>" in xml
    assert "<cbc:Description>Service A</cbc:Description>" in xml
    assert "<cbc:Description>Service B</cbc:Description>" in xml


def test_invoice_build_with_party_details():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        AccountingSupplierParty=AccountingSupplierParty(
            Party=Party(
                PartyName=PartyName(Name="ACME Corp"),
                PartyIdentification=[
                    PartyIdentification(ID="12345678", schemeID="VAT"),
                    PartyIdentification(ID="US123456", schemeID="EIN"),
                ],
                Contact=Contact(
                    Name="John Doe",
                    Telephone="+1-555-1234",
                    ElectronicMail="john@acme.com",
                ),
                PostalAddress=Address(
                    StreetName="123 Main St",
                    BuildingNumber="100",
                    CityName="New York",
                    PostalZone="10001",
                    Country=Country(IdentificationCode="US"),
                ),
            )
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(
                PartyName=PartyName(Name="Client Inc"),
                PartyIdentification=[
                    PartyIdentification(ID="87654321", schemeID="VAT"),
                ],
            )
        ),
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="100.00", currencyID="EUR")
        ),
        invoiceLine=[
            InvoiceLine(
                ID="1",
                LineExtensionAmount=LineExtensionAmount(
                    value="100.00", currencyID="EUR"
                ),
                Item=Item(Description="Service"),
            )
        ],
    ).build()

    assert etree.tostring(invoice, encoding="unicode").startswith(
        '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"'
    )
    assert "<cbc:Name>ACME Corp</cbc:Name>" in etree.tostring(
        invoice, encoding="unicode"
    )


def test_invoice_build_with_delivery():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        Delivery=[
            Delivery(
                ID="DEL-001",
                ActualDeliveryDate="2017-12-05",
                DeliveryAddress=Address(
                    StreetName="456 Delivery St",
                    CityName="Los Angeles",
                    PostalZone="90001",
                    Country=Country(IdentificationCode="US"),
                ),
            )
        ],
        AccountingSupplierParty=AccountingSupplierParty(
            Party=Party(PartyName=PartyName(Name="Seller Co"))
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(PartyName=PartyName(Name="Buyer Co"))
        ),
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="100.00", currencyID="EUR")
        ),
        invoiceLine=[
            InvoiceLine(
                ID="1",
                LineExtensionAmount=LineExtensionAmount(
                    value="100.00", currencyID="EUR"
                ),
                Item=Item(Description="Service"),
            )
        ],
    ).build()

    xml = etree.tostring(invoice, encoding="unicode")
    assert "<cbc:ID>DEL-001</cbc:ID>" in xml
    assert "<cbc:ActualDeliveryDate>2017-12-05</cbc:ActualDeliveryDate>" in xml


def test_invoice_build_with_allowance_charge():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        AllowanceCharge=[
            AllowanceCharge(
                ChargeIndicator="true",
                AllowanceChargeReason="Handling fee",
                Amount=PayableAmount(value="10.00", currencyID="EUR"),
                BaseAmount=PayableAmount(value="100.00", currencyID="EUR"),
            )
        ],
        AccountingSupplierParty=AccountingSupplierParty(
            Party=Party(PartyName=PartyName(Name="Seller Co"))
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(PartyName=PartyName(Name="Buyer Co"))
        ),
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="110.00", currencyID="EUR")
        ),
        invoiceLine=[
            InvoiceLine(
                ID="1",
                LineExtensionAmount=LineExtensionAmount(
                    value="100.00", currencyID="EUR"
                ),
                Item=Item(Description="Service"),
            )
        ],
    ).build()

    xml = etree.tostring(invoice, encoding="unicode")
    assert "<cbc:ChargeIndicator>true</cbc:ChargeIndicator>" in xml
    assert "<cbc:AllowanceChargeReason>Handling fee</cbc:AllowanceChargeReason>" in xml


def test_invoice_build_validates_against_ubl_xsd():
    this_folder_path = Path(__file__).resolve().parents[0]
    invoice_xsd = (
        this_folder_path / "schemas" / "xsd" / "maindoc" / "UBL-Invoice-2.1.xsd"
    )

    schema_doc = etree.parse(str(invoice_xsd))
    schema = etree.XMLSchema(schema_doc)

    invoice = Invoice(
        ID="1",
        IssueDate="2024-01-01",
        AccountingSupplierParty=AccountingSupplierParty(
            Party=Party(PartyName=PartyName(Name="Seller Co"))
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(PartyName=PartyName(Name="Buyer Co"))
        ),
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="100.00", currencyID="EUR")
        ),
        invoiceLine=[
            InvoiceLine(
                ID="1",
                LineExtensionAmount=LineExtensionAmount(
                    value="100.00", currencyID="EUR"
                ),
                Item=Item(Description="Service"),
            )
        ],
    ).build()

    schema.assertValid(invoice)
