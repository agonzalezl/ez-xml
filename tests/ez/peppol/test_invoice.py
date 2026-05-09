from ez.peppol import (
    AccountingCustomerParty,
    AccountingSupplierParty,
    ClassifiedTaxCategory,
    Contact,
    Country,
    EndpointID,
    ID,
    Invoice,
    InvoiceLine,
    InvoicedQuantity,
    Item,
    LegalMonetaryTotal,
    LineExtensionAmount,
    Location,
    Party,
    PartyIdentification,
    PartyLegalEntity,
    PartyName,
    PartyTaxScheme,
    PayableAmount,
    PostalAddress,
    Price,
    PriceAmount,
    TaxAmount,
    TaxCategory,
    TaxExclusiveAmount,
    TaxInclusiveAmount,
    TaxScheme,
    TaxSubtotal,
    TaxTotal,
    TaxableAmount,
)
from lxml import etree, objectify
from pathlib import Path
from saxonche import PySaxonProcessor


def test_invoice_build_validates_against_peppol_schematron():
    """Test invoice validates against Peppol BIS 3.0 Schematron rules"""

    # Build minimal valid Peppol invoice
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
                PartyIdentification=[PartyIdentification(ID=ID("1548079098355"))],
                PartyName=PartyName(Name="Seller Ltd"),
                Contact=Contact(
                    Name="John Doe",
                    Telephone="+44-123-456-789",
                    ElectronicMail="john@seller.com",
                ),
                PostalAddress=PostalAddress(
                    StreetName="123 Main St",
                    CityName="London",
                    PostalZone="SW1A 1AA",
                    Country=Country(IdentificationCode="GB"),
                ),
                PartyLegalEntity=[PartyLegalEntity(RegistrationName="Seller LTD")],
                PhysicalLocation=Location(
                    ID="123",
                ),
                PartyTaxScheme=PartyTaxScheme(
                    CompanyID="GB123456789", TaxScheme=TaxScheme(ID="VAT")
                ),
            )
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(
                EndpointID=EndpointID("1548079098355", schemeID="0088"),
                PartyName=PartyName(Name="Buyer Inc"),
                PostalAddress=PostalAddress(
                    CityName="Berlin",
                    PostalZone="10115",
                    Country=Country(IdentificationCode="DE"),
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
                            ID="S", Percent="20", TaxScheme=TaxScheme(ID="VAT")
                        ),
                    )
                ],
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
                LineExtensionAmount=LineExtensionAmount(
                    value="100.00", currencyID="EUR"
                ),
                Item=Item(
                    Description="Services",
                    Name="Services",
                    ClassifiedTaxCategory=ClassifiedTaxCategory(ID="S", Percent="20"),
                ),
                InvoicedQuantity=InvoicedQuantity(value="1", unitCode="C62"),
                Price=Price(PriceAmount=PriceAmount(value="100.00", currencyID="EUR")),
            ),
        ],
    ).build()

    xml_string = etree.tostring(invoice, encoding="unicode", pretty_print=True)

    this_folder_path = Path(__file__).resolve().parents[0]

    schematron_xsl = this_folder_path / "schematron" / "PEPPOL-EN16931-UBL.xsl"
    report = validate_with_schematron_xsl(xml_string, str(schematron_xsl))
    peppol_errors, peppol_warnings = extract_failed_asserts(report)

    schematron_xsl = this_folder_path / "schematron" / "CEN-EN16931-UBL.xsl"
    report = validate_with_schematron_xsl(xml_string, str(schematron_xsl))
    cen_errors, cen_warnings = extract_failed_asserts(report)

    assert (peppol_errors + cen_errors) == []
    assert (peppol_warnings + cen_warnings) == []


def test_invoice_build():
    invoice = Invoice(
        ID="12345",
        IssueDate="2017-12-01",
        InvoiceTypeCode="1",
        Note="Note",
        DocumentCurrencyCode="eur",
        BuyerReference="N/A",
        AccountingSupplierParty=AccountingSupplierParty(
            Party=Party(
                EndpointID=EndpointID("1548079098355", schemeID="0088"),
                PartyIdentification=[PartyIdentification(ID=ID("1548079098355"))],
                PartyName=PartyName(Name="Seller Co"),
                PartyLegalEntity=[PartyLegalEntity(RegistrationName="Seller CO")],
                PartyTaxScheme=PartyTaxScheme(
                    CompanyID="GB123456789", TaxScheme=TaxScheme(ID="VAT")
                ),
                PostalAddress=PostalAddress(
                    CityName="Berlin",
                    PostalZone="10115",
                    Country=Country(IdentificationCode="DE"),
                ),
            )
        ),
        AccountingCustomerParty=AccountingCustomerParty(
            Party=Party(
                EndpointID=EndpointID("1548079098355", schemeID="0088"),
                PartyName=PartyName(Name="Buyer Co"),
                PartyLegalEntity=[PartyLegalEntity(RegistrationName="Buyer CO")],
                PostalAddress=PostalAddress(
                    CityName="Berlin",
                    PostalZone="10115",
                    Country=Country(IdentificationCode="DE"),
                ),
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
                            ID="S", Percent="20", TaxScheme=TaxScheme(ID="VAT")
                        ),
                    )
                ],
            )
        ],
        LegalMonetaryTotal=LegalMonetaryTotal(
            LineExtensionAmount=LineExtensionAmount(value="100.00", currencyID="EUR"),
            TaxExclusiveAmount=TaxExclusiveAmount(value="90.00", currencyID="EUR"),
            PayableAmount=PayableAmount(value="100.00", currencyID="EUR"),
            TaxInclusiveAmount=TaxInclusiveAmount(value="120.00", currencyID="EUR"),
        ),
        InvoiceLines=[
            InvoiceLine(
                ID="123",
                LineExtensionAmount=LineExtensionAmount(
                    value="50.00", currencyID="EUR"
                ),
                Item=Item(
                    Description="Service A",
                    Name="Service A",
                    ClassifiedTaxCategory=ClassifiedTaxCategory(ID="S", Percent="25"),
                ),
                InvoicedQuantity=InvoicedQuantity(value="1", unitCode="C62"),
                Price=Price(PriceAmount=PriceAmount(value="50.00", currencyID="EUR")),
            ),
            InvoiceLine(
                ID="456",
                LineExtensionAmount=LineExtensionAmount(
                    value="50.00", currencyID="EUR"
                ),
                Item=Item(
                    Description="Service B",
                    Name="Service B",
                    ClassifiedTaxCategory=ClassifiedTaxCategory(ID="S", Percent="25"),
                ),
                InvoicedQuantity=InvoicedQuantity(value="1", unitCode="C62"),
                Price=Price(PriceAmount=PriceAmount(value="50.00", currencyID="EUR")),
            ),
        ],
    ).build()

    xml = etree.tostring(invoice, encoding="unicode", pretty_print=True)

    assert (
        xml.strip()
        == """<Invoice xmlns:qdt="urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2" xmlns:ccts="urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2" xmlns:stat="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusCode-1.0" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:udt="urn:un:unece:uncefact:data:draft:UnqualifiedDataTypesSchemaModule:2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">
  <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</cbc:ProfileID>
  <cbc:ID>12345</cbc:ID>
  <cbc:IssueDate>2017-12-01</cbc:IssueDate>
  <cbc:InvoiceTypeCode>1</cbc:InvoiceTypeCode>
  <cbc:Note>Note</cbc:Note>
  <cbc:DocumentCurrencyCode>eur</cbc:DocumentCurrencyCode>
  <cbc:BuyerReference>N/A</cbc:BuyerReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:EndpointID schemeID="0088">1548079098355</cbc:EndpointID>
      <cac:PartyIdentification>
        <cbc:ID>1548079098355</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Seller Co</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:CityName>Berlin</cbc:CityName>
        <cbc:PostalZone>10115</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>GB123456789</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Seller CO</cbc:RegistrationName>
      </cac:PartyLegalEntity>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cbc:EndpointID schemeID="0088">1548079098355</cbc:EndpointID>
      <cac:PartyName>
        <cbc:Name>Buyer Co</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:CityName>Berlin</cbc:CityName>
        <cbc:PostalZone>10115</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>DE</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Buyer CO</cbc:RegistrationName>
      </cac:PartyLegalEntity>
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
    <cbc:LineExtensionAmount currencyID="EUR">100.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="EUR">90.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="EUR">120.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="EUR">100.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>123</cbc:ID>
    <cbc:InvoicedQuantity unitCode="C62">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Service A</cbc:Description>
      <cbc:Name>Service A</cbc:Name>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>25</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="EUR">50.00</cbc:PriceAmount>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>456</cbc:ID>
    <cbc:InvoicedQuantity unitCode="C62">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="EUR">50.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Service B</cbc:Description>
      <cbc:Name>Service B</cbc:Name>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>25</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="EUR">50.00</cbc:PriceAmount>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>""".strip()
    )


def validate_with_schematron_xsl(xml_string: str, schematron_xsl_path: str):
    with PySaxonProcessor(license=False) as proc:
        xslt30_processor = proc.new_xslt30_processor()
        input_node = proc.parse_xml(xml_text=xml_string)
        executable = xslt30_processor.compile_stylesheet(
            stylesheet_file=str(schematron_xsl_path)
        )
        report = executable.transform_to_string(xdm_node=input_node)
        return report.encode("utf-8")


def extract_failed_asserts(xml: bytes) -> tuple[list[str], list[str]]:
    root = objectify.fromstring(xml)
    failed_asserts = root.xpath(
        "//svrl:failed-assert/svrl:text",
        namespaces={"svrl": "http://purl.oclc.org/dsdl/svrl"},
    )
    warnings = root.xpath(
        "//svrl:successful-report/svrl:text",
        namespaces={"svrl": "http://purl.oclc.org/dsdl/svrl"},
    )
    errors = [
        failed_assert.text.strip()
        for failed_assert in failed_asserts
        if failed_assert.text
    ]
    warnings = [warning.text.strip() for warning in warnings if warning.text]
    return errors, warnings
