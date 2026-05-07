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
