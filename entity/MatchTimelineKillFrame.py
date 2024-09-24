from sqlalchemy import Column, String, Integer, BigInteger, Text, DateTime, UniqueConstraint, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql import func

Base = declarative_base()

class MatchTimelineKillFrame(Base):
  __tablename__ = 'match_timeline_kill_frame'

  id = Column(BigInteger, primary_key=True, autoincrement=True)
  matchId = Column(String(50), nullable=True)
  videoId = Column(BigInteger, nullable=True)
  eventTime = Column(Integer, nullable=True)
  positionX = Column(Integer, nullable=True)
  positionY = Column(Integer, nullable=True)
  killerPuuid = Column(String(255), nullable=True)
  killerPlayerAccountId = Column(BigInteger, nullable=True)
  killerChampion = Column(String(255), nullable=True)
  assistPuuids = Column(LONGTEXT(collation='utf8mb4_bin'), nullable=True)
  assistChampions = Column(LONGTEXT(collation='utf8mb4_bin'), nullable=True, comment='JSON Array')
  victimPuuid = Column(String(255), nullable=True)
  victimPlayerAccountId = Column(BigInteger, nullable=True)
  victimChampion = Column(String(255), nullable=True)
  victimDamageDealt = Column(LONGTEXT(collation='utf8mb4_bin'), nullable=True, comment='JSON Object')
  victimDamageReceived = Column(LONGTEXT(collation='utf8mb4_bin'), nullable=True, comment='JSON Object')
  bounty = Column(Integer, nullable=True)
  shutdownBounty = Column(Integer, nullable=True)
  killStreakLength = Column(Integer, nullable=True)
  createdDatetime = Column(DateTime, nullable=False, default=func.now())
  updatedDatetime = Column(DateTime, nullable=True, onupdate=func.now())

