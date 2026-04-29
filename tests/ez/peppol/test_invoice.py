from ez.peppol._invoice import Invoice
from ez.ubl._invoice import (
    InvoiceLine,
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
)
from lxml import etree


def test_invoice_build():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        InvoiceTypeCode="1",
        Note="Note",
        DocumentCurrencyCode="eur",
        BuyerReference="N/A",
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
        InvoiceLines=[
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

    xml = etree.tostring(invoice, encoding="unicode", pretty_print=True)

    assert (
        xml.strip()
        == """<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">
  <CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</CustomizationID>
  <ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</ProfileID>
  <cbc:ID>12345</cbc:ID>
  <cbc:IssueDate>2017-12-01</cbc:IssueDate>
  <cbc:InvoiceTypeCode>1</cbc:InvoiceTypeCode>
  <cbc:Note>Note</cbc:Note>
  <cbc:DocumentCurrencyCode>eur</cbc:DocumentCurrencyCode>
  <cbc:BuyerReference>N/A</cbc:BuyerReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Seller Co</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Buyer Co</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="EUR">20.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="EUR">100.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="EUR">20.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:PayableAmount currencyID="EUR">120.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>123</cbc:ID>
    <cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Service A</cbc:Description>
    </cac:Item>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>456</cbc:ID>
    <cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Service B</cbc:Description>
    </cac:Item>
  </cac:InvoiceLine>
</Invoice>""".strip()
    )
