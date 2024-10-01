from ez.ubl._invoice import Invoice
from lxml import etree


def test_invoice_build():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        Note="Note",
    ).build()

    assert (
        etree.tostring(invoice, encoding="unicode")
        == '<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">'
        "<cbc:ID>12345</cbc:ID>"
        "<cbc:IssueDate>2017-12-01</cbc:IssueDate>"
        "<cbc:Note>Note</cbc:Note>"
        "</Invoice>"
    )
