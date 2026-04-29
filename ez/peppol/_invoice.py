from ez.ubl._invoice import Invoice as UBLInvoice
import dataclasses
from ez.xml.model import nsmap, EzField
from ez.ubl._constants import NS_MAP


@nsmap(NS_MAP)
@dataclasses.dataclass(kw_only=True)
class Invoice(UBLInvoice):
    CustomizationID: str = (
        "urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0"
    )
    ProfileID: str = "urn:fdc:peppol.eu:2017:poacc:billing:01:1.0"
    # BuyerReference is mandatory in Peppol BIS 3.0 (see DE-R-015)
    BuyerReference: str = EzField("cbc")
