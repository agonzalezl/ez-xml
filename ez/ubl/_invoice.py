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


@nsmap(NS_MAP)
@dataclasses.dataclass()
class Invoice(EzXMLModel):
    ID: str = EzField("cbc")
    IssueDate: str = EzField("cbc")
    Note: str = EzField("cbc")
    OrderReference: OrderReference
