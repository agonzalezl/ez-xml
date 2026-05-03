from __future__ import annotations
from ez.ubl._invoice import Invoice as UBLInvoice
from ez.ubl._invoice import AccountingSupplierParty as UBLAccountingSupplierParty
from ez.xml.model import EzXMLModel
from ez.ubl._invoice import (
    PartyName,
    PartyIdentification,
    PartyLegalEntity,
    Contact,
    Address,
    Location,
)

import dataclasses
from ez.xml.model import nsmap, EzField
from ez.ubl._constants import NS_MAP


@dataclasses.dataclass(kw_only=True)
class Party(EzXMLModel):
    """
    Party does not inherit UBLParty cause then we have problems with reordering of the parameters
    Problem that should be solved by using pydantic instead
    """

    _ns = "cac"
    EndpointID: str = EzField("cbc")
    PartyIdentification: list[PartyIdentification] | None = None
    PartyName: PartyName | None = None
    PostalAddress: Address | None = None
    # TODO: PartyTaxScheme
    PartyLegalEntity: list[PartyLegalEntity] | None = None
    Contact: Contact | None = None
    PhysicalLocation: Location | None = None


@dataclasses.dataclass()
class AccountingSupplierParty(UBLAccountingSupplierParty):
    Party: Party


@nsmap(NS_MAP)
@dataclasses.dataclass(kw_only=True)
class Invoice(UBLInvoice):
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
