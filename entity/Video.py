from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, Text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Video(Base):
  __tablename__ = "video"
  id = Column(Integer, primary_key=True)
  localFileName = Column(String(200))
  playSeconds = Column(Integer)
  youtubeTitle = Column(String(255))
  youtubeDescription = Column(Text)
  youtubeUri = Column(Text)
  state = Column(String(30), default='WAIT_VIDEO', nullable=False)