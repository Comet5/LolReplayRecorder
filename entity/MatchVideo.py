from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, Text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class MatchVideo(Base):
  __tablename__ = "match_video"
  id = Column(Integer, primary_key=True)
  matchTimelineKillFrameId = Column(Integer, nullable=False)
  matchId = Column(String(255), nullable=False)
  youtubeTitle = Column(String(255))
  youtubeDescription = Column(Text)
  youtubeUri = Column(Text)
  state = Column(String(30), default='WAIT_VIDEO', nullable=False)