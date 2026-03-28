from ez.ubl._invoice import (
    Invoice,
    InvoiceLine,
    OrderReference,
    AccountingSupplierParty,
    AccountingCustomerParty,
    LegalMonetaryTotal,
)
from lxml import etree


def test_invoice_build():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        InvoiceTypeCode="1",
        DocumentCurrencyCode="eur",
        Note="Note",
        orderReference=OrderReference(
            ID="1111111111",
            SalesOrderID="aaaaaaaaa",
            UUID="2222222",
            IssueDate="2017-12-01",
        ),
        AccountingSupplierParty=AccountingSupplierParty(),
        AccountingCustomerParty=AccountingCustomerParty(),
        TaxTotal="123",
        LegalMonetaryTotal=LegalMonetaryTotal(),
        invoiceLine=[InvoiceLine(ID="123"), InvoiceLine(ID="456")]
    ).build()

    assert (
        etree.tostring(invoice, encoding="unicode")
        == '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">'
        "<cbc:ID>12345</cbc:ID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "<cbc:InvoiceTypeCode>1</cbc:InvoiceTypeCode>"
        "<cbc:DocumentCurrencyCode>eur</cbc:DocumentCurrencyCode>"
        "<cbc:Note>Note</cbc:Note>"
        "<cac:OrderReference>"
        "<cbc:ID>1111111111</cbc:ID>"
        "<cbc:SalesOrderID>aaaaaaaaa</cbc:SalesOrderID>"
        "<cbc:UUID>2222222</cbc:UUID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "</cac:OrderReference>"
        "<cac:AccountingSupplierParty/>"
        "<cac:AccountingCustomerParty/>"
        "<cbc:TaxTotal>123</cbc:TaxTotal>"
        "<cac:LegalMonetaryTotal/>"
        "<cac:InvoiceLine><cbc:ID>123</cbc:ID></cac:InvoiceLine><cac:InvoiceLine><cbc:ID>456</cbc:ID></cac:InvoiceLine>"
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
        AccountingSupplierParty=AccountingSupplierParty(),
        AccountingCustomerParty=AccountingCustomerParty(),
        TaxTotal="123",
        LegalMonetaryTotal=LegalMonetaryTotal(),
        invoiceLine=[InvoiceLine(ID="123"), InvoiceLine(ID="456")]
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
        "<cac:AccountingSupplierParty/>"
        "<cac:AccountingCustomerParty/>"
        "<cbc:TaxTotal>123</cbc:TaxTotal>"
        "<cac:LegalMonetaryTotal/>"
        "<cac:InvoiceLine><cbc:ID>123</cbc:ID></cac:InvoiceLine><cac:InvoiceLine><cbc:ID>456</cbc:ID></cac:InvoiceLine>"
        "</Invoice>"
    )
