from ez import ubl

import dataclasses
from ez.xml.model import EzField


@dataclasses.dataclass()
class TaxScheme(ubl.CacEntity):
    ID: str = EzField("cbc")


TaxSchemeType = TaxScheme


@dataclasses.dataclass()
class PartyTaxScheme(ubl.CacEntity):
    CompanyID: str = EzField("cbc")
    TaxScheme: TaxSchemeType


PartyTaxSchemeType = PartyTaxScheme


@dataclasses.dataclass()
class PartyLegalEntity(ubl.PartyLegalEntity):
    RegistrationName: str = EzField("cbc")


PartyLegalEntityType = PartyLegalEntity


@dataclasses.dataclass(kw_only=True)
class PostalAddress(ubl.Address): ...


PostalAddressType = PostalAddress


@dataclasses.dataclass()
class EndpointID(ubl.CbcEntity):
    value: str
    schemeID: str | None = EzField(type="attribute", default=None)


EndpointIDType = EndpointID


@dataclasses.dataclass(kw_only=True)
class Party(ubl.CacEntity):
    """
    Redeclared and not inheriting ubl.Party due to the need of altering the original order of the fields
    """

    EndpointID: EndpointIDType
    PartyIdentification: list[ubl.PartyIdentification] | None = None
    PartyName: ubl.PartyName | None = None
    PostalAddress: PostalAddressType
    PartyTaxScheme: PartyTaxSchemeType | None = None
    PartyLegalEntity: list[PartyLegalEntityType]
    Contact: ubl.Contact | None = None
    PhysicalLocation: ubl.Location | None = None


@dataclasses.dataclass()
class AccountingSupplierParty(ubl.AccountingSupplierParty):
    Party: Party


@dataclasses.dataclass()
class TaxExclusiveAmount(ubl.CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


TaxExclusiveAmountType = TaxExclusiveAmount


@dataclasses.dataclass()
class TaxInclusiveAmount(ubl.CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


TaxInclusiveAmountType = TaxInclusiveAmount


@dataclasses.dataclass()
class LegalMonetaryTotal(ubl.CacEntity):
    LineExtensionAmount: ubl.LineExtensionAmount
    TaxExclusiveAmount: TaxExclusiveAmountType
    TaxInclusiveAmount: TaxInclusiveAmountType
    PayableAmount: ubl.PayableAmount


LegalMonetaryTotalType = LegalMonetaryTotal


@dataclasses.dataclass()
class InvoicedQuantity(ubl.CbcEntity):
    value: str
    unitCode: str = EzField(type="attribute")


InvoicedQuantityType = InvoicedQuantity


@dataclasses.dataclass()
class PriceAmount(ubl.CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


PriceAmountType = PriceAmount


@dataclasses.dataclass()
class Price(ubl.CacEntity):
    PriceAmount: PriceAmountType


PriceType = Price


@dataclasses.dataclass()
class ClassifiedTaxCategory(ubl.CacEntity):
    ID: str = EzField("cbc")
    Percent: str | None = EzField("cbc", default=None)
    TaxScheme: ubl.TaxScheme = dataclasses.field(
        default_factory=lambda: ubl.TaxScheme(ID="VAT")
    )


ClassifiedTaxCategoryType = ClassifiedTaxCategory


@dataclasses.dataclass(kw_only=True)
class Item(ubl.Item):
    Description: str | None = EzField("cbc", default=None)
    Name: str = EzField("cbc")
    ClassifiedTaxCategory: ClassifiedTaxCategoryType


ItemType = Item


@dataclasses.dataclass(kw_only=True)
class InvoiceLine(ubl.CacEntity):
    ID: str = EzField("cbc")
    Note: str | None = EzField("cbc", default=None)
    InvoicedQuantity: InvoicedQuantityType
    LineExtensionAmount: ubl.LineExtensionAmount
    DocumentReference: list[ubl.DocumentReference] | None = None
    AllowanceCharge: list[ubl.AllowanceCharge] | None = None
    Item: ItemType
    Price: PriceType


InvoiceLineType = InvoiceLine


@dataclasses.dataclass(kw_only=True)
class Invoice(ubl.Invoice):
    CustomizationID: str = EzField(
        "cbc",
        default="urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0",
    )
    ProfileID: str = EzField(
        "cbc", default="urn:fdc:peppol.eu:2017:poacc:billing:01:1.0"
    )
    # BuyerReference is mandatory in Peppol BIS 3.0 (see DE-R-015)
    BuyerReference: str = EzField("cbc")
    AccountingSupplierParty: AccountingSupplierParty
    LegalMonetaryTotal: LegalMonetaryTotalType
    InvoiceLines: list[InvoiceLine]
