import time

import requests
from api.LolClientApi import LolClientApi
import config.DbConnection as db
from entity.Match import Match
from entity.Player import Player


# targetNickname = 'Hide on bush'
#
# clientApi.focusChampionByNickname(targetNickname)
# clientApi.moveTime(999999)
# time.sleep(1)
# clientApi.moveTime(15)
#
#
# events = clientApi.getEvents()
# for event in events:
#   if event['EventName'] == 'ChampionKill':
#     if targetNickname in event['Assisters'] or targetNickname == event['KillerName']:
#       print(event)
  # print(event)
  # print(event['Assisters'])


clientApi = LolClientApi()

with db.session() as session:  # execute until yield. Session is yielded value
  # players = session.query(Player).all()
  # for player in players:
  #   print(player.name)

  matches = session.query(Match.matchId).order_by(Match.playDatetime.desc()).limit(500).all()
  for match in matches:
    clientApi.downloadReplay(match.matchId.split('_')[1])
    time.sleep(1)

