import time

import requests
from sqlalchemy import func

from api.LolClientApi import LolClientApi
import common.DbConnection as db
from entity.LolVersion import LolVersion
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

# Download Replay
with db.session() as session:
  max_game_version = session.query(func.max(LolVersion.version)).scalar()
  print(max_game_version)

  matches = session.query(Match.id, Match.matchId).filter(Match.gameVersion == max_game_version, Match.replayDownloaded == False).order_by(Match.playDatetime.desc()).all()
  print(f'Found {len(matches)} matches')
  for match in matches:
    clientApi.downloadReplay(match.matchId.split('_')[1])
    session.query(Match).filter(Match.id == match.id).update({Match.replayDownloaded: True})
    time.sleep(1)



