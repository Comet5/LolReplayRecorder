from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Match:
    id: Optional[int] = None
    playerAccountId: Optional[int] = None
    matchId: Optional[str] = None
    gameDuration: Optional[int] = None
    gameMode: Optional[str] = None
    gameName: Optional[str] = None
    gameType: Optional[str] = None
    gameVersion: Optional[str] = None
    platformId: Optional[str] = None
    queueId: Optional[int] = None
    mapId: Optional[int] = None
    teamsJson: Optional[str] = None
    participantsJson: Optional[str] = None
    playDatetime: Optional[date] = None
    createdDatetime: date = None
    updatedDatetime: Optional[date] = None
