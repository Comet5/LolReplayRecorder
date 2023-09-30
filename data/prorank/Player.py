from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Player:
    id: Optional[int] = None
    teamId: Optional[str] = None
    name: str = None
    nativeName: Optional[str] = None
    nickname: str = None
    nicknameFull: Optional[str] = None
    country: Optional[str] = None
    role: Optional[str] = None
    residency: Optional[str] = None
    birthdate: Optional[str] = None
    age: Optional[int] = None
    sns: Optional[str] = None
    isRetired: Optional[bool] = None
    photoUri: Optional[str] = None
    createdDatetime: date = None
    updatedDatetime: Optional[date] = None

