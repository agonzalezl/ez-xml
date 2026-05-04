from ez.xml.model_pydantic import PydanticEzXMLModel, EzField
from ._constants import NS_MAP


class UblEntity(PydanticEzXMLModel):
    _nsmap = NS_MAP


class CacEntity(UblEntity):
    _ns = "cac"


class CbcEntity(UblEntity):
    _ns = "cbc"


class PartyIdentification(CacEntity):
    ID: str
    schemeID: str | None = EzField(type="attribute")


PartyIdentificationType = PartyIdentification


class PayableAmount(CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


PayableAmountType = PayableAmount


class OrderReference(CacEntity):
    ID: str = EzField("cbc")
    SalesOrderID: str = EzField("cbc")
    UUID: str = EzField("cbc")
    IssueDate: str = EzField("cbc")


OrderReferenceType = OrderReference


class PartyLegalEntity(CacEntity):
    RegistrationName: str | None = EzField("cbc", default=None)
    CompanyID: str | None = EzField("cbc", default=None)
    CompanyLegalForm: str | None = EzField("cbc", default=None)
    CompanyLegalFormCode: str | None = EzField("cbc", default=None)
    CurrencyCode: str | None = EzField("cbc", default=None)


PartyLegalEntityType = PartyLegalEntity


class DocumentReference(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    DocumentTypeCode: str | None = EzField("cbc", default=None)
    URI: str | None = EzField("cbc", default=None)
    IssueDate: str | None = EzField("cbc", default=None)
    IssueTime: str | None = EzField("cbc", default=None)
    DocumentType: str | None = EzField("cbc", default=None)
    LanguageCode: str | None = EzField("cbc", default=None)
    CategoryCode: str | None = EzField("cbc", default=None)


DocumentReferenceType = DocumentReference


class PartyName(CacEntity):
    Name: str = EzField("cbc")


PartyNameType = PartyName


class Contact(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    Telephone: str | None = EzField("cbc", default=None)
    Telefax: str | None = EzField("cbc", default=None)
    ElectronicMail: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    OtherCommunication: str | None = EzField("cbc", default=None)


ContactType = Contact


class FinancialAccount(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    AccountTypeCode: str | None = EzField("cbc", default=None)
    AccountNumber: str | None = EzField("cbc", default=None)
    CurrencyCode: str | None = EzField("cbc", default=None)
    PaymentNote: str | None = EzField("cbc", default=None)


class TaxableAmount(CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


class LegalMonetaryTotal(CacEntity):
    PayableAmount: PayableAmountType


LegalMonetaryTotalType = LegalMonetaryTotal


class LineExtensionAmount(CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


class Country(CacEntity):
    IdentificationCode: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)


CountryType = Country


class Address(CacEntity):
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
    Country: CountryType | None = None


AddressType = Address


class Location(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)
    CountrySubentity: str | None = EzField("cbc", default=None)
    Address: AddressType | None = None


class Party(CacEntity):
    PartyName: PartyNameType | None = None
    PartyIdentification: list[PartyIdentificationType] | None = None
    PartyLegalEntity: list[PartyLegalEntityType] | None = None
    Contact: ContactType | None = None
    PostalAddress: Address | None = None
    PhysicalLocation: Location | None = None


PartyType = Party


class AccountingSupplierParty(CacEntity):
    Party: PartyType | None = None
    CustomerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


AccountingSupplierPartyType = AccountingSupplierParty


class AccountingCustomerParty(CacEntity):
    Party: PartyType | None = None
    CustomerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


class PayeeParty(CacEntity):
    PartyName: PartyNameType | None = None
    PartyIdentification: list[PartyIdentificationType] | None = None
    PartyLegalEntity: list[PartyLegalEntityType] | None = None
    Contact: ContactType | None = None
    PostalAddress: Address | None = None


PayeePartyType = PayeeParty


class BuyerCustomerParty(CacEntity):
    Party: PartyType | None = None
    DeliveryContact: Contact | None = None
    AccountingContact: Contact | None = None
    BuyerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


BuyerCustomerPartyType = BuyerCustomerParty


class SellerSupplierParty(CacEntity):
    Party: PartyType | None = None
    DeliveryContact: Contact | None = None
    AccountingContact: Contact | None = None
    BuyerAssignedAccountID: str | None = EzField("cbc", default=None)
    SupplierAssignedAccountID: str | None = EzField("cbc", default=None)


SellerSupplierPartyType = SellerSupplierParty


class TaxRepresentativeParty(CacEntity):
    PartyName: PartyNameType | None = None
    PartyIdentification: list[PartyIdentificationType] | None = None
    PartyLegalEntity: list[PartyLegalEntityType] | None = None
    Contact: ContactType | None = None
    PostalAddress: Address | None = None


TaxRepresentativePartyType = TaxRepresentativeParty


class TaxAmount(CbcEntity):
    value: str
    currencyID: str = EzField(type="attribute")


TaxAmountType = TaxAmount


class TaxScheme(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    TaxTypeCode: str | None = EzField("cbc", default=None)
    CurrencyCode: str | None = EzField("cbc", default=None)


TaxSchemeType = TaxScheme


class ExchangeRate(CacEntity):
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


class Period(CacEntity):
    StartDate: str | None = EzField("cbc", default=None)
    StartTime: str | None = EzField("cbc", default=None)
    EndDate: str | None = EzField("cbc", default=None)
    EndTime: str | None = EzField("cbc", default=None)
    DurationMeasure: str | None = EzField("cbc", default=None)
    DescriptionCode: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)


class InvoicePeriod(CacEntity):
    StartDate: str | None = EzField("cbc", default=None)
    StartTime: str | None = EzField("cbc", default=None)
    EndDate: str | None = EzField("cbc", default=None)
    EndTime: str | None = EzField("cbc", default=None)
    DurationMeasure: str | None = EzField("cbc", default=None)
    DescriptionCode: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)


InvoicePeriodType = InvoicePeriod


class BillingReference(CacEntity):
    InvoiceDocumentReference: DocumentReference | None = None


BillingReferenceType = BillingReference


class ProjectReference(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    UUID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    Description: str | None = EzField("cbc", default=None)


ProjectReferenceType = ProjectReference


class DeliveryTerms(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    SpecialTransportTerms: str | None = EzField("cbc", default=None)
    LossRiskResponsibilityCode: str | None = EzField("cbc", default=None)
    LossRisk: str | None = EzField("cbc", default=None)
    DeliveryLocation: Location | None = None


DeliveryTermsType = DeliveryTerms


class PaymentTerms(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    PaymentMeansID: str | None = EzField("cbc", default=None)
    PaymentDueDate: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    ReferenceEventCode: str | None = EzField("cbc", default=None)
    SettlementPeriod: Period | None = None


PaymentTermsType = PaymentTerms


class PaymentMeans(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    PaymentMeansCode: str | None = EzField("cbc", default=None)
    PaymentDueDate: str | None = EzField("cbc", default=None)
    PaymentChannelCode: str | None = EzField("cbc", default=None)
    InstructionNote: str | None = EzField("cbc", default=None)
    PaymentID: str | None = EzField("cbc", default=None)
    FinanicalAccount: FinancialAccount | None = None
    CreditAccount: FinancialAccount | None = None
    CardAccount: FinancialAccount | None = None


PaymentMeansType = PaymentMeans


class PrepaidPayment(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    PaidAmount: PayableAmount | None = None
    ReceivedDate: str | None = EzField("cbc", default=None)
    PaidDate: str | None = EzField("cbc", default=None)
    InstructionNote: str | None = EzField("cbc", default=None)


PrepaidPaymentType = PrepaidPayment


class Delivery(CacEntity):
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
    DeliveryTerms: DeliveryTermsType | None = None


DeliveryType = Delivery


class AllowanceCharge(CacEntity):
    ChargeIndicator: str | None = EzField("cbc", default=None)
    AllowanceChargeReasonCode: str | None = EzField("cbc", default=None)
    AllowanceChargeReason: str | None = EzField("cbc", default=None)
    Amount: PayableAmount | None = None
    BaseAmount: PayableAmount | None = None
    PerUnitAmount: PayableAmount | None = None
    SequenceNumeric: str | None = EzField("cbc", default=None)


AllowanceChargeType = AllowanceCharge


class TaxExchangeRate(CacEntity):
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


TaxExchangeRateType = TaxExchangeRate


class PricingExchangeRate(CacEntity):
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


PricingExchangeRateType = PricingExchangeRate


class PaymentExchangeRate(CacEntity):
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


PaymentExchangeRateType = PaymentExchangeRate


class PaymentAlternativeExchangeRate(CacEntity):
    SourceCurrencyCode: str | None = EzField("cbc", default=None)
    TargetCurrencyCode: str | None = EzField("cbc", default=None)
    Rate: str | None = EzField("cbc", default=None)
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    MarketIdentifierCode: str | None = EzField("cbc", default=None)
    ContractCurrencyCode: str | None = EzField("cbc", default=None)


PaymentAlternativeExchangeRateType = PaymentAlternativeExchangeRate


class TaxCategory(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    Name: str | None = EzField("cbc", default=None)
    Percent: str | None = EzField("cbc", default=None)
    TaxExemptionReasonCode: str | None = EzField("cbc", default=None)
    TaxExemptionReason: str | None = EzField("cbc", default=None)
    TierRange: str | None = EzField("cbc", default=None)
    TaxScheme: TaxSchemeType | None = None


TaxCategoryType = TaxCategory


class TaxSubtotal(CacEntity):
    taxableAmount: TaxableAmount | None = None
    taxAmount: TaxAmount | None = None
    CalculationSequenceNumeric: str | None = EzField("cbc", default=None)
    TransactionCurrencyTaxAmount: str | None = EzField("cbc", default=None)
    Percent: str | None = EzField("cbc", default=None)
    BaseUnitMeasure: str | None = EzField("cbc", default=None)
    PerUnitAmount: PayableAmount | None = None
    TaxCategory: TaxCategoryType | None = None


TaxSubtotalType = TaxSubtotal


class TaxTotal(CacEntity):
    TaxAmount: TaxAmountType | None = None
    RoundingAmount: PayableAmount | None = None
    TaxEvidenceIndicator: str | None = EzField("cbc", default=None)
    TaxIncludedIndicator: str | None = EzField("cbc", default=None)
    TaxSubtotal: list[TaxSubtotalType] | None = None


TaxTotalType = TaxTotal


class WithholdingTaxTotal(CacEntity):
    TaxAmount: TaxAmountType | None = None
    RoundingAmount: PayableAmount | None = None
    TaxEvidenceIndicator: str | None = EzField("cbc", default=None)
    TaxIncludedIndicator: str | None = EzField("cbc", default=None)
    TaxSubtotal: list[TaxSubtotalType] | None = None


WithholdingTaxTotalType = WithholdingTaxTotal


class Signature(CacEntity):
    ID: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    ReferencedSignatureID: str | None = EzField("cbc", default=None)
    SignedBy: Party | None = None


SignatureType = Signature


class Item(CacEntity):
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


class InvoiceLine(CacEntity):
    ID: str = EzField("cbc")
    lineExtensionAmount: LineExtensionAmount
    item: Item
    UUID: str | None = EzField("cbc", default=None)
    Note: str | None = EzField("cbc", default=None)
    InvoicedQuantity: str | None = EzField("cbc", default=None)
    DocumentReference: list[DocumentReferenceType] | None = None
    PricingReference: str | None = EzField("cac", default=None)
    Delivery: DeliveryType | None = None
    TaxTotal: list[TaxTotalType] | None = None
    WithholdingTaxTotal: list[WithholdingTaxTotalType] | None = None
    AllowanceCharge: list[AllowanceChargeType] | None = None


class Invoice(UblEntity):
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
    InvoicePeriod: InvoicePeriodType | None = None
    OrderReference: OrderReferenceType | None = None
    BillingReference: list[BillingReferenceType] | None = None
    DespatchDocumentReference: list[DocumentReference] | None = None
    ReceiptDocumentReference: list[DocumentReference] | None = None
    StatementDocumentReference: list[DocumentReference] | None = None
    OriginatorDocumentReference: list[DocumentReference] | None = None
    ContractDocumentReference: list[DocumentReference] | None = None
    AdditionalDocumentReference: list[DocumentReference] | None = None
    ProjectReference: list[ProjectReferenceType] | None = None
    Signature: list[SignatureType] | None = None
    AccountingSupplierParty: AccountingSupplierPartyType
    AccountingCustomerParty: AccountingCustomerParty
    PayeeParty: PayeePartyType | None = None
    BuyerCustomerParty: BuyerCustomerPartyType | None = None
    SellerSupplierParty: SellerSupplierPartyType | None = None
    TaxRepresentativeParty: TaxRepresentativePartyType | None = None
    Delivery: list[DeliveryType] | None = None
    DeliveryTerms: DeliveryTermsType | None = None
    PaymentMeans: list[PaymentMeansType] | None = None
    PaymentTerms: list[PaymentTermsType] | None = None
    PrepaidPayment: list[PrepaidPaymentType] | None = None
    AllowanceCharge: list[AllowanceChargeType] | None = None
    TaxExchangeRate: TaxExchangeRateType | None = None
    PricingExchangeRate: PricingExchangeRateType | None = None
    PaymentExchangeRate: PaymentExchangeRateType | None = None
    PaymentAlternativeExchangeRate: PaymentAlternativeExchangeRateType | None = None
    TaxTotal: list[TaxTotalType] | None = None
    WithholdingTaxTotal: list[WithholdingTaxTotalType] | None = None
    LegalMonetaryTotal: LegalMonetaryTotalType
    InvoiceLines: list[InvoiceLine]
