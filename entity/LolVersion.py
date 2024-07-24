from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class LolVersion(Base):
  __tablename__ = "lol_version"
  id = Column(Integer, primary_key=True)
  version = Column(String(100), nullable=False, unique=True)
  created_datetime = Column(DateTime, nullable=False)

  def __init__(self, version, created_datetime):
    self.version = version
    self.created_datetime = created_datetime
