import json

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Position:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y


class Event:
  def __init__(self, type: str, timestamp: int, assistingParticipantIds: list, killStreakLength: int, killerId: int, position: Position, shutdownBounty: int, victimId: int):
    self.type = type
    self.timestamp = timestamp
    self.assistingParticipantIds = assistingParticipantIds
    self.killStreakLength = killStreakLength
    self.killerId = killerId
    self.position = position
    self.shutdownBounty = shutdownBounty
    self.victimId = victimId


class MatchTimeline(Base):
  __tablename__ = "match_timeline"
  id = Column(Integer, primary_key=True)
  matchId = Column(String(50), nullable=False)
  _eventJson = Column('eventJson', Text, nullable=False)
  createdDatetime = Column(DateTime, nullable=False)
  updatedDatetime = Column(DateTime)

  @hybrid_property
  def eventJson(self):
    data = json.loads(self._eventJson)
    events = []
    for item in data:
      position = Position(item['position']['x'], item['position']['y'])
      event = Event(item['type'], item['timestamp'], item['assistingParticipantIds'], item['killStreakLength'], item['killerId'], position, item['shutdownBounty'], item['victimId'])
      events.append(event)
    return events

  @eventJson.setter
  def eventJson(self, value):
    self._eventJson = json.dumps([vars(e) for e in value])
