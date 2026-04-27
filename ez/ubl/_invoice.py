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
class PartyName(EzXMLModel):
    _ns = "cac"
    Name: str = EzField("cbc")


@dataclasses.dataclass()
class Party(EzXMLModel):
    _ns = "cac"
    PartyName: PartyName


@dataclasses.dataclass()
class AccountingSupplierParty(EzXMLModel):
    _ns = "cac"
    Party: Party


@dataclasses.dataclass()
class AccountingCustomerParty(EzXMLModel):
    _ns = "cac"
    Party: Party


@dataclasses.dataclass()
class PayableAmount(EzXMLModel):
    _ns = "cbc"
    value: str
    currencyID: str = EzField(type="attribute")


@dataclasses.dataclass()
class LegalMonetaryTotal(EzXMLModel):
    _ns = "cac"
    PayableAmount: PayableAmount


@dataclasses.dataclass()
class LineExtensionAmount(EzXMLModel):
    _ns = "cbc"
    value: str
    currencyID: str = EzField(type="attribute")


@dataclasses.dataclass()
class Item(EzXMLModel):
    _ns = "cac"
    Description: str = EzField("cbc")


@dataclasses.dataclass()
class InvoiceLine(EzXMLModel):
    _ns = "cac"
    ID: str = EzField("cbc")
    LineExtensionAmount: LineExtensionAmount
    Item: Item


@nsmap(NS_MAP)
@dataclasses.dataclass(kw_only=True)
class Invoice(EzXMLModel):
    CustomizationID: str | None = EzField("cbc", default=None)
    ProfileID: str | None = EzField("cbc", default=None)
    ProfileExecutionID: str | None = EzField("cbc", default=None)
    ID: str = EzField("cbc")
    CopyIndicator: str | None = EzField("cbc", default=None)
    UUID: str | None = EzField("cbc", default=None)
    IssueDate: str = EzField("cbc")
    IssueTime: str | None = EzField("cbc", default=None)
    DueDate: str | None = EzField("cbc", default=None)
    InvoiceTypeCode: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    TaxPointDate: str | None = EzField("cbc", default=None)
    DocumentCurrencyCode: str | None = EzField("cbc", default=None)
    TaxCurrencyCode: str | None = EzField("cbc", default=None)
    PricingCurrencyCode: str | None = EzField("cbc", default=None)
    PaymentCurrencyCode: str | None = EzField("cbc", default=None)
    PaymentAlternativeCurrencyCode: str | None = EzField("cbc", default=None)
    AccountingCostCode: str | None = EzField("cbc", default=None)
    AccountingCost: str | None = EzField("cbc", default=None)
    LineCountNumeric: str | None = EzField("cbc", default=None)
    BuyerReference: str | None = EzField("cbc", default=None)
    InvoicePeriod: str | None = EzField("cac", default=None)
    orderReference: OrderReference | None = None
    BillingReference: str | None = EzField("cac", default=None)
    DespatchDocumentReference: str | None = EzField("cac", default=None)
    AccountingSupplierParty: AccountingSupplierParty
    AccountingCustomerParty: AccountingCustomerParty
    PaymentAlternativeExchangeRate: str | None = EzField("cac", default=None)
    TaxTotal: str | None = EzField("cac", default=None)
    WithholdingTaxTotal: str | None = EzField("cac", default=None)
    LegalMonetaryTotal: LegalMonetaryTotal
    invoiceLine: list[InvoiceLine]
