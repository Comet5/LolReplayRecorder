import datetime

import config
from service.LcuService import LcuService
import service.DiscordService as discord

# targetNicknames = ['Jiwoo']
targetNicknames = ['Chovy', 'Peyz', 'Kiin', 'Canyon', 'Faker', 'ShowMaker',
                   'Zeus', 'Oner', 'Gumayusi', 'Keria', 'Morgan']

discord = discord.DiscordService()
try:
  lcu = LcuService()
  lcu.run_league_of_legends()
  lcu.download_replay(targetNicknames, datetime.datetime.now() - datetime.timedelta(days=2))
except Exception as e:
  discord.send_discord_webhook(config.DISCORD_WEBHOOK_URI, f"Replay Download Failed: {e}")
  raise e




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

