import dataclasses
from ez.xml.model import EzXMLModel, nsmap, EzField
from ._constants import NS_MAP


@nsmap(NS_MAP)
@dataclasses.dataclass()
class Invoice(EzXMLModel):
    ID: str = EzField("cbc")
    IssueDate: str = EzField("cbc")
    Note: str = EzField("cbc")
