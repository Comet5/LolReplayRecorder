import time
import datetime

from cv2 import matchShapes

from api.LolClientApi import LolClientApi
import common.DbConnection as db
from entity.LolVersion import LolVersion
from entity.Match import Match
from entity.MatchVideo import MatchVideo
from entity.Player import Player
from entity.PlayerAccount import PlayerAccount


clientApi = LolClientApi()
targetNicknames = ['Chovy', 'Peyz', 'Kiin', 'Canyon', 'Faker', 'ShowMaker', 'Zeus', 'Oner', 'Gumayusi', 'Keria']

with (db.session() as session):
  players = session.query(Player).filter(Player.nickname.in_(targetNicknames)).all()
  for player in players:
    print(player.nickname)
    player_accounts = session.query(PlayerAccount).filter(PlayerAccount.playerId == player.id).all()
    for player_account in player_accounts:
      print(f'\t{player_account.summonerName}')
      matches = session.query(Match).outerjoin(
          MatchVideo, Match.matchId == MatchVideo.matchId
      ).filter(
          MatchVideo.matchId == None  # Filter where MatchVideo does not exist
      ).filter(
          Match.playerAccountId == player_account.id
      ).filter(
          Match.replayDownloaded == 0
      ).filter(
          Match.playDatetime >= datetime.datetime.now() - datetime.timedelta(days=2)
      ).all()

      for match in matches:
        clientApi.downloadReplay(match.matchId.split('_')[1])
        match.replayDownloaded = 1
        time.sleep(0.1)
  session.commit()

# # Match Replay 데이터 다운로드
# for match in targetMatches:
#   print(match)
#   clientApi.downloadReplay(match.matchId.split('_')[1])
#   with db.session() as session:
#     # update match.replayDownloaded
#     match.replayDownloaded = 1
#     session.commit()

# with db.session() as session:
#   matchVideo = MatchVideo(matchId=matchId, state='WAIT_VIDEO')
#   session.add(matchVideo)
#   session.commit()











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


# clientApi = LolClientApi()
# res = clientApi.watchReplay("6571041847")
# print(res)


# import os
# import subprocess

# Define the RADS_PATH


# with db.session() as session:  # execute until yield. Session is yielded value
#   # players = session.query(Player).all()
#   # for player in players:
#   #   print(player.name)
#
#   matches = session.query(Match.matchId).order_by(Match.playDatetime.desc()).limit(500).all()
#   for match in matches:
#     clientApi.downloadReplay(match.matchId.split('_')[1])
#     time.sleep(1)

