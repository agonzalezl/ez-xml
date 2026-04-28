from __future__ import annotations
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
    PartyName: PartyName | None = None
    PartyIdentification: list[PartyIdentification] | None = None
    PartyLegalEntity: list[PartyLegalEntity] | None = None
    Contact: Contact | None = None
    PostalAddress: Address | None = None
    PhysicalLocation: Location | None = None


@dataclasses.dataclass()
class AccountingSupplierParty(EzXMLModel):
    _ns = "cac"
    Party: Party | None = None
    CustomerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class AccountingCustomerParty(EzXMLModel):
    _ns = "cac"
    Party: Party | None = None
    CustomerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class PayeeParty(EzXMLModel):
    _ns = "cac"
    PartyName: PartyName | None = None
    PartyIdentification: list[PartyIdentification] | None = None
    PartyLegalEntity: list[PartyLegalEntity] | None = None
    Contact: Contact | None = None
    PostalAddress: Address | None = None


@dataclasses.dataclass()
class BuyerCustomerParty(EzXMLModel):
    _ns = "cac"
    Party: Party | None = None
    DeliveryContact: Contact | None = None
    AccountingContact: Contact | None = None
    BuyerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class SellerSupplierParty(EzXMLModel):
    _ns = "cac"
    Party: Party | None = None
    DeliveryContact: Contact | None = None
    AccountingContact: Contact | None = None
    BuyerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class TaxRepresentativeParty(EzXMLModel):
    _ns = "cac"
    PartyName: PartyName | None = None
    PartyIdentification: list[PartyIdentification] | None = None
    PartyLegalEntity: list[PartyLegalEntity] | None = None
    Contact: Contact | None = None
    PostalAddress: Address | None = None


@dataclasses.dataclass()
class PayableAmount(EzXMLModel):
    _ns = "cbc"
    value: str
    currencyID: str = EzField(type="attribute")


@dataclasses.dataclass()
class TaxAmount(EzXMLModel):
    _ns = "cbc"
    value: str
    currencyID: str = EzField(type="attribute")


@dataclasses.dataclass()
class TaxableAmount(EzXMLModel):
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
class Country(EzXMLModel):
    _ns = "cac"
    IdentificationCode: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class Address(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    AddressTypeCode: str | None = EzField("cbc", default=None)
    StreetName: str | None = EzField("cbc", default=None)
    BuildingNumber: str | None = EzField("cbc", default=None)
    AdditionalStreetName: str | None = EzField("cbc", default=None)
    CityName: str | None = EzField("cbc", default=None)
    PostalZone: str | None = EzField("cbc", default=None)
    CountrySubentity: str | None = EzField("cbc", default=None)
    CountrySubentityCode: str | None = EzField("cbc", default=None)
    Region: str | None = EzField("cbc", default=None)
    District: str | None = EzField("cbc", default=None)
    Floor: str | None = EzField("cbc", default=None)
    Room: str | None = EzField("cbc", default=None)
    BlockName: str | None = EzField("cbc", default=None)
    Building: str | None = EzField("cbc", default=None)
    InhouseMail: str | None = EzField("cbc", default=None)
    Country: Country | None = None


@dataclasses.dataclass()
class Contact(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    Telephone: str | None = EzField("cbc", default=None)
    Telefax: str | None = EzField("cbc", default=None)
    ElectronicMail: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    OtherCommunication: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class PartyIdentification(EzXMLModel):
    _ns = "cac"
    ID: str
    schemeID: str | None = EzField(type="attribute")


@dataclasses.dataclass()
class PartyLegalEntity(EzXMLModel):
    _ns = "cac"
    RegistrationName: str | None = EzField("cbc", default=None)
    CompanyID: str | None = EzField("cbc", default=None)
    CompanyLegalForm: str | None = EzField("cbc", default=None)
    CompanyLegalFormCode: str | None = EzField("cbc", default=None)
    CurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class FinancialAccount(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    AccountTypeCode: str | None = EzField("cbc", default=None)
    AccountNumber: str | None = EzField("cbc", default=None)
    CurrencyCode: str | None = EzField("cbc", default=None)
    PaymentNote: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class Location(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)
    CountrySubentity: str | None = EzField("cbc", default=None)
    Address: Address | None = None


@dataclasses.dataclass()
class TaxScheme(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    TaxTypeCode: str | None = EzField("cbc", default=None)
    CurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class ExchangeRate(EzXMLModel):
    _ns = "cac"
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class Period(EzXMLModel):
    _ns = "cac"
    StartDate: str | None = EzField("cbc", default=None)
    StartTime: str | None = EzField("cbc", default=None)
    EndDate: str | None = EzField("cbc", default=None)
    EndTime: str | None = EzField("cbc", default=None)
    DurationMeasure: str | None = EzField("cbc", default=None)
    DescriptionCode: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class InvoicePeriod(EzXMLModel):
    _ns = "cac"
    StartDate: str | None = EzField("cbc", default=None)
    StartTime: str | None = EzField("cbc", default=None)
    EndDate: str | None = EzField("cbc", default=None)
    EndTime: str | None = EzField("cbc", default=None)
    DurationMeasure: str | None = EzField("cbc", default=None)
    DescriptionCode: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class DocumentReference(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    DocumentTypeCode: str | None = EzField("cbc", default=None)
    URI: str | None = EzField("cbc", default=None)
    IssueDate: str | None = EzField("cbc", default=None)
    IssueTime: str | None = EzField("cbc", default=None)
    DocumentType: str | None = EzField("cbc", default=None)
    LanguageCode: str | None = EzField("cbc", default=None)
    CategoryCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class BillingReference(EzXMLModel):
    _ns = "cac"
    InvoiceDocumentReference: DocumentReference | None = None


@dataclasses.dataclass()
class ProjectReference(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    UUID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class DeliveryTerms(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    SpecialTransportTerms: str | None = EzField("cbc", default=None)
    LossRiskResponsibilityCode: str | None = EzField("cbc", default=None)
    LossRisk: str | None = EzField("cbc", default=None)
    DeliveryLocation: Location | None = None


@dataclasses.dataclass()
class PaymentTerms(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    PaymentMeansID: str | None = EzField("cbc", default=None)
    PaymentDueDate: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    ReferenceEventCode: str | None = EzField("cbc", default=None)
    SettlementPeriod: Period | None = None


@dataclasses.dataclass()
class PaymentMeans(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    PaymentMeansCode: str | None = EzField("cbc", default=None)
    PaymentDueDate: str | None = EzField("cbc", default=None)
    PaymentChannelCode: str | None = EzField("cbc", default=None)
    InstructionNote: str | None = EzField("cbc", default=None)
    PaymentID: str | None = EzField("cbc", default=None)
    FinanicalAccount: FinancialAccount | None = None
    CreditAccount: FinancialAccount | None = None
    CardAccount: FinancialAccount | None = None


@dataclasses.dataclass()
class PrepaidPayment(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    PaidAmount: PayableAmount | None = None
    ReceivedDate: str | None = EzField("cbc", default=None)
    PaidDate: str | None = EzField("cbc", default=None)
    InstructionNote: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class Delivery(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Quantity: str | None = EzField("cbc", default=None)
    MinimumQuantity: str | None = EzField("cbc", default=None)
    MaximumQuantity: str | None = EzField("cbc", default=None)
    ActualDeliveryDate: str | None = EzField("cbc", default=None)
    ActualDeliveryTime: str | None = EzField("cbc", default=None)
    LatestDeliveryDate: str | None = EzField("cbc", default=None)
    LatestDeliveryTime: str | None = EzField("cbc", default=None)
    ReleaseID: str | None = EzField("cbc", default=None)
    TrackingID: str | None = EzField("cbc", default=None)
    DeliveryAddress: Address | None = None
    DeliveryLocation: Location | None = None
    AlternativeDeliveryLocation: Location | None = None
    RequestedDeliveryPeriod: Period | None = None
    PromisedDeliveryPeriod: Period | None = None
    EstimatedDeliveryPeriod: Period | None = None
    CarrierParty: Party | None = None
    DeliveryParty: Party | None = None
    NotifyParty: Party | None = None
    DeliveryTerms: DeliveryTerms | None = None


@dataclasses.dataclass()
class AllowanceCharge(EzXMLModel):
    _ns = "cac"
    ChargeIndicator: str | None = EzField("cbc", default=None)
    AllowanceChargeReasonCode: str | None = EzField("cbc", default=None)
    AllowanceChargeReason: str | None = EzField("cbc", default=None)
    Amount: PayableAmount | None = None
    BaseAmount: PayableAmount | None = None
    PerUnitAmount: PayableAmount | None = None
    SequenceNumeric: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class TaxExchangeRate(EzXMLModel):
    _ns = "cac"
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class PricingExchangeRate(EzXMLModel):
    _ns = "cac"
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class PaymentExchangeRate(EzXMLModel):
    _ns = "cac"
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class PaymentAlternativeExchangeRate(EzXMLModel):
    _ns = "cac"
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


@dataclasses.dataclass()
class TaxCategory(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    Percent: str | None = EzField("cbc", default=None)
    TaxExemptionReasonCode: str | None = EzField("cbc", default=None)
    TaxExemptionReason: str | None = EzField("cbc", default=None)
    TierRange: str | None = EzField("cbc", default=None)
    TaxScheme: TaxScheme | None = None


@dataclasses.dataclass()
class TaxSubtotal(EzXMLModel):
    _ns = "cac"
    TaxableAmount: TaxableAmount | None = None
    TaxAmount: TaxAmount | None = None
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    TransactionCurrencyTaxAmount: str | None = EzField("cbc", default=None)
    Percent: str | None = EzField("cbc", default=None)
    BaseUnitMeasure: str | None = EzField("cbc", default=None)
    PerUnitAmount: PayableAmount | None = None
    TaxCategory: TaxCategory | None = None


@dataclasses.dataclass()
class TaxTotal(EzXMLModel):
    _ns = "cac"
    TaxAmount: TaxAmount | None = None
    RoundingAmount: PayableAmount | None = None
    TaxEvidenceIndicator: str | None = EzField("cbc", default=None)
    TaxIncludedIndicator: str | None = EzField("cbc", default=None)
    TaxSubtotal: list[TaxSubtotal] | None = None


@dataclasses.dataclass()
class WithholdingTaxTotal(EzXMLModel):
    _ns = "cac"
    TaxAmount: TaxAmount | None = None
    RoundingAmount: PayableAmount | None = None
    TaxEvidenceIndicator: str | None = EzField("cbc", default=None)
    TaxIncludedIndicator: str | None = EzField("cbc", default=None)
    TaxSubtotal: list[TaxSubtotal] | None = None


@dataclasses.dataclass()
class Signature(EzXMLModel):
    _ns = "cac"
    ID: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    ReferencedSignatureID: str | None = EzField("cbc", default=None)
    SignedBy: Party | None = None


@dataclasses.dataclass()
class Item(EzXMLModel):
    _ns = "cac"
    Description: str | None = EzField("cbc", default=None)
    PackQuantity: str | None = EzField("cbc", default=None)
    PackSizeNumeric: str | None = EzField("cbc", default=None)
    CatalogueIndicator: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    HazardousRiskIndicator: str | None = EzField("cbc", default=None)
    AdditionalInformation: str | None = EzField("cbc", default=None)
    Keyword: str | None = EzField("cbc", default=None)
    BrandName: str | None = EzField("cbc", default=None)
    ModelName: str | None = EzField("cbc", default=None)
    SellersItemIdentification: PartyIdentification | None = None
    BuyersItemIdentification: PartyIdentification | None = None
    StandardItemIdentification: PartyIdentification | None = None
    OriginAddress: Address | None = None
    OriginCountry: Country | None = None


@dataclasses.dataclass(kw_only=True)
class InvoiceLine(EzXMLModel):
    _ns = "cac"
    ID: str = EzField("cbc")
    LineExtensionAmount: LineExtensionAmount
    Item: Item
    UUID: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    InvoicedQuantity: str | None = EzField("cbc", default=None)
    DocumentReference: list[DocumentReference] | None = None
    PricingReference: str | None = EzField("cac", default=None)
    Delivery: Delivery | None = None
    TaxTotal: list[TaxTotal] | None = None
    WithholdingTaxTotal: list[WithholdingTaxTotal] | None = None
    AllowanceCharge: list[AllowanceCharge] | None = None


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
    InvoicePeriod: InvoicePeriod | None = None
    OrderReference: OrderReference | None = None
    BillingReference: list[BillingReference] | None = None
    DespatchDocumentReference: list[DocumentReference] | None = None
    ReceiptDocumentReference: list[DocumentReference] | None = None
    StatementDocumentReference: list[DocumentReference] | None = None
    OriginatorDocumentReference: list[DocumentReference] | None = None
    ContractDocumentReference: list[DocumentReference] | None = None
    AdditionalDocumentReference: list[DocumentReference] | None = None
    ProjectReference: list[ProjectReference] | None = None
    Signature: list[Signature] | None = None
    AccountingSupplierParty: AccountingSupplierParty
    AccountingCustomerParty: AccountingCustomerParty
    PayeeParty: PayeeParty | None = None
    BuyerCustomerParty: BuyerCustomerParty | None = None
    SellerSupplierParty: SellerSupplierParty | None = None
    TaxRepresentativeParty: TaxRepresentativeParty | None = None
    Delivery: list[Delivery] | None = None
    DeliveryTerms: DeliveryTerms | None = None
    PaymentMeans: list[PaymentMeans] | None = None
    PaymentTerms: list[PaymentTerms] | None = None
    PrepaidPayment: list[PrepaidPayment] | None = None
    AllowanceCharge: list[AllowanceCharge] | None = None
    TaxExchangeRate: TaxExchangeRate | None = None
    PricingExchangeRate: PricingExchangeRate | None = None
    PaymentExchangeRate: PaymentExchangeRate | None = None
    PaymentAlternativeExchangeRate: PaymentAlternativeExchangeRate | None = None
    TaxTotal: list[TaxTotal] | None = None
    WithholdingTaxTotal: list[WithholdingTaxTotal] | None = None
    LegalMonetaryTotal: LegalMonetaryTotal
    invoiceLine: list[InvoiceLine]
