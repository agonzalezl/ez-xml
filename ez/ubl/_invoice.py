import dataclasses
from ez.xml.model import EzXMLModel, nsmap, EzField
from ._constants import NS_MAP


@dataclasses.dataclass()
class OrderReference(EzXMLModel):
    _ns = "cac"
    ID: str = EzField("cbc")
    SalesOrderID: str = EzField("cbc")
    UUID: str = EzField("cbc")
    IssueDate: str = EzField("cbc")


@dataclasses.dataclass()
class AccountingSupplierParty(EzXMLModel):
    _ns = "cac"


@dataclasses.dataclass()
class AccountingCustomerParty(EzXMLModel):
    _ns = "cac"


@dataclasses.dataclass()
class LegalMonetaryTotal(EzXMLModel):
    _ns = "cac"

@dataclasses.dataclass()
class InvoiceLine(EzXMLModel):
    _ns = "cac"
    ID: str = EzField("cbc")

@nsmap(NS_MAP)
@dataclasses.dataclass(kw_only=True)
class Invoice(EzXMLModel):
    ID: str = EzField("cbc")
    IssueDate: str = EzField("cbc")
    InvoiceTypeCode: str = EzField("cbc")
    DocumentCurrencyCode: str = EzField("cbc")
    Note: str | None = EzField("cbc", default=None)
    orderReference: OrderReference | None = None
    AccountingSupplierParty: AccountingSupplierParty
    AccountingCustomerParty: AccountingCustomerParty
    TaxTotal: str = EzField("cbc")
    LegalMonetaryTotal: LegalMonetaryTotal
    invoiceLine: list[InvoiceLine]
