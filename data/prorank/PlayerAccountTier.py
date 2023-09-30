from dataclasses import dataclass
from datetime import date
from typing import Optional

from data import RiotEnum


@dataclass
class PlayerAccountTier:
    id: Optional[int] = None
    playerAccountId: Optional[int] = None
    season: Optional[str] = None
    queueType: Optional[RiotEnum.QueueType] = None
    tier: Optional[str] = None
    rank: Optional[str] = None
    leaguePoints: Optional[int] = None
    wins: Optional[int] = None
    looses: Optional[int] = None
    hotStreak: Optional[bool] = None
    veteran: Optional[bool] = None
    freshBlood: Optional[bool] = None
    inactive: Optional[bool] = None
    miniSeriesTarget: Optional[int] = None
    miniSeriesWins: Optional[int] = None
    miniSeriesLooses: Optional[int] = None
    miniSeriesProgress: Optional[str] = None
    createdDatetime: Optional[date] = None
    updatedDatetime: Optional[date] = None


