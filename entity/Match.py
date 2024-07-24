from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, Text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Match(Base):
  __tablename__ = "match"
  id = Column(Integer, primary_key=True)
  playerAccountId = Column(Integer)
  matchId = Column(String(50), nullable=False)
  gameDuration = Column(Integer)
  gameMode = Column(String(50))
  gameName = Column(String(50))
  gameType = Column(String(50))
  gameVersion = Column(String(50))
  platformId = Column(String(20))
  queueId = Column(Integer)
  mapId = Column(Integer)
  teamsJson = Column(Text)
  participantsJson = Column(Text)
  playDatetime = Column(DateTime, nullable=False)
  createdDatetime = Column(DateTime, nullable=False)
  updatedDatetime = Column(DateTime)
  replayDownloaded = Column(Boolean, nullable=False)
  sceneDownloaded = Column(Boolean, nullable=False)

