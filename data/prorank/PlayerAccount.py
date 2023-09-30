from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class PlayerAccount:
    id: Optional[int] = None
    playerId: Optional[int] = None
    region: Optional[str] = None
    summonerId: Optional[str] = None
    puuid: Optional[str] = None
    accountId: Optional[str] = None
    summonerName: Optional[str] = None
    summonerLevel: Optional[int] = None
    profileIconId: Optional[int] = None
    status: Optional[str] = None
    latestPlayedDatetime: Optional[date] = None
    createdDatetime: Optional[date] = None
    updatedDatetime: Optional[date] = None
