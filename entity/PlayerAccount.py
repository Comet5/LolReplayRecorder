from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, Text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class PlayerAccount(Base):
  __tablename__ = "player_account"
  id = Column(Integer, primary_key=True)
  playerId = Column(Integer)
  region = Column(String(20))
  summonerId = Column(String(100))
  puuid = Column(String(100))
  accountId = Column(String(100))
  summonerName = Column(String(50), nullable=False)
  tagLine = Column(String(15), nullable=False)
  summonerLevel = Column(Integer)
  profileIconId = Column(Integer)
  status = Column(Integer, default=1)
  latestPlayedDatetime = Column(DateTime)
  createdDatetime = Column(DateTime, nullable=False)
  updatedDatetime = Column(DateTime)