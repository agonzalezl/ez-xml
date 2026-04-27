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
        orderReference=OrderReference(
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
        TaxTotal="123",
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="100.00", currencyID="EUR")
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

    assert (
        etree.tostring(invoice, encoding="unicode")
        == '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">'
        "<cbc:ID>12345</cbc:ID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "<cbc:InvoiceTypeCode>1</cbc:InvoiceTypeCode>"
        "<cbc:Note>Note</cbc:Note>"
        "<cbc:DocumentCurrencyCode>eur</cbc:DocumentCurrencyCode>"
        "<cac:OrderReference>"
        "<cbc:ID>1111111111</cbc:ID>"
        "<cbc:SalesOrderID>aaaaaaaaa</cbc:SalesOrderID>"
        "<cbc:UUID>2222222</cbc:UUID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "</cac:OrderReference>"
        "<cac:AccountingSupplierParty>"
        "<cac:Party><cac:PartyName><cbc:Name>Seller Co</cbc:Name></cac:PartyName></cac:Party>"
        "</cac:AccountingSupplierParty>"
        "<cac:AccountingCustomerParty>"
        "<cac:Party><cac:PartyName><cbc:Name>Buyer Co</cbc:Name></cac:PartyName></cac:Party>"
        "</cac:AccountingCustomerParty>"
        "<cac:TaxTotal>123</cac:TaxTotal>"
        '<cac:LegalMonetaryTotal><cbc:PayableAmount currencyID="EUR">100.00</cbc:PayableAmount></cac:LegalMonetaryTotal>'
        '<cac:InvoiceLine><cbc:ID>123</cbc:ID><cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount><cac:Item><cbc:Description>Service A</cbc:Description></cac:Item></cac:InvoiceLine>'
        '<cac:InvoiceLine><cbc:ID>456</cbc:ID><cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount><cac:Item><cbc:Description>Service B</cbc:Description></cac:Item></cac:InvoiceLine>'
        "</Invoice>"
    )


def test_invoice_build_optional():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        InvoiceTypeCode="1",
        DocumentCurrencyCode="eur",
        orderReference=OrderReference(
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
        TaxTotal="123",
        LegalMonetaryTotal=LegalMonetaryTotal(
            PayableAmount=PayableAmount(value="100.00", currencyID="EUR")
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

    assert (
        etree.tostring(invoice, encoding="unicode")
        == '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">'
        "<cbc:ID>12345</cbc:ID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "<cbc:InvoiceTypeCode>1</cbc:InvoiceTypeCode>"
        "<cbc:DocumentCurrencyCode>eur</cbc:DocumentCurrencyCode>"
        "<cac:OrderReference>"
        "<cbc:ID>1111111111</cbc:ID>"
        "<cbc:SalesOrderID>aaaaaaaaa</cbc:SalesOrderID>"
        "<cbc:UUID>2222222</cbc:UUID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "</cac:OrderReference>"
        "<cac:AccountingSupplierParty>"
        "<cac:Party><cac:PartyName><cbc:Name>Seller Co</cbc:Name></cac:PartyName></cac:Party>"
        "</cac:AccountingSupplierParty>"
        "<cac:AccountingCustomerParty>"
        "<cac:Party><cac:PartyName><cbc:Name>Buyer Co</cbc:Name></cac:PartyName></cac:Party>"
        "</cac:AccountingCustomerParty>"
        "<cac:TaxTotal>123</cac:TaxTotal>"
        '<cac:LegalMonetaryTotal><cbc:PayableAmount currencyID="EUR">100.00</cbc:PayableAmount></cac:LegalMonetaryTotal>'
        '<cac:InvoiceLine><cbc:ID>123</cbc:ID><cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount><cac:Item><cbc:Description>Service A</cbc:Description></cac:Item></cac:InvoiceLine>'
        '<cac:InvoiceLine><cbc:ID>456</cbc:ID><cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount><cac:Item><cbc:Description>Service B</cbc:Description></cac:Item></cac:InvoiceLine>'
        "</Invoice>"
    )


def test_invoice_build_validates_against_ubl_xsd():
    this_folder_path = Path(__file__).resolve().parents[0]
    invoice_xsd = (
        this_folder_path /"schemas" / "xsd" / "maindoc" / "UBL-Invoice-2.1.xsd"
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

    assert (
        etree.tostring(invoice, encoding="unicode")
        == '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">'
        "<cbc:ID>1</cbc:ID>"
        "<cbc:IssueDate>2024-01-01</cbc:IssueDate>"
        "<cac:AccountingSupplierParty>"
        "<cac:Party><cac:PartyName><cbc:Name>Seller Co</cbc:Name></cac:PartyName></cac:Party>"
        "</cac:AccountingSupplierParty>"
        "<cac:AccountingCustomerParty>"
        "<cac:Party><cac:PartyName><cbc:Name>Buyer Co</cbc:Name></cac:PartyName></cac:Party>"
        "</cac:AccountingCustomerParty>"
        '<cac:LegalMonetaryTotal><cbc:PayableAmount currencyID="EUR">100.00</cbc:PayableAmount></cac:LegalMonetaryTotal>'
        '<cac:InvoiceLine><cbc:ID>1</cbc:ID><cbc:LineExtensionAmount currencyID="EUR">100.00</cbc:LineExtensionAmount><cac:Item><cbc:Description>Service</cbc:Description></cac:Item></cac:InvoiceLine>'
        "</Invoice>"
    )

    schema.assertValid(invoice)
