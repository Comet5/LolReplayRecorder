from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, Text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Player(Base):
  __tablename__ = "player"
  id = Column(Integer, primary_key=True)
  teamId = Column(Integer)
  name = Column(String(100), nullable=False)
  nativeName = Column(String(100))
  nickname = Column(String(100), nullable=False)
  nicknameFull = Column(String(100), nullable=False)
  country = Column(String(100))
  residency = Column(String(100))
  role = Column(String(100))
  birthdate = Column(Date)
  age = Column(SmallInteger)
  sns = Column(Text, comment=';으로 구분, Discord;Facebook;Instagram;Reddit;Snapchat;Stream;Twitter;Vk;Website;Weibo;Youtube;')
  photoUri = Column(String(200))
  isRetired = Column(Boolean, nullable=False)
  createdDatetime = Column(DateTime, nullable=False)
  updatedDatetime = Column(DateTime)