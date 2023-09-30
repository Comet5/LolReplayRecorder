from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Team:
    name: str
    nameShort: Optional[str]
    region: str
    sns: Optional[str]
    isDisbanded: Optional[bool]
    createdDatetime: Optional[date]
    id: Optional[int] = None
    nameFull: Optional[str] = None
    logoUri: Optional[str] = None
    renamedTeamId: Optional[int] = None
    updatedDatetime: Optional[date] = None

