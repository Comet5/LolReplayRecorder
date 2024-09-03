import time

import requests
from sqlalchemy import func

from api.LolClientApi import LolClientApi
import common.DbConnection as db
from entity.LolVersion import LolVersion
from entity.Match import Match
from entity.MatchTimeline import MatchTimeline
from entity.Player import Player
import os
import subprocess

import config
from service.LcuService import LcuService
import service.DiscordService as discord


discord = discord.DiscordService()
try:
  lcu = LcuService()
  lcu.run_league_of_legends()
  lcu.run_replay('7257757677')
except Exception as e:
  discord.send_discord_webhook(config.DISCORD_WEBHOOK_URI, f"Replay Download Failed: {e}")
  raise e

# # Download Replay
# with (db.session() as session):
#   max_game_version = session.query(func.max(LolVersion.version)).scalar()
#   print(max_game_version)
#
#   matches = session.query(
#       Match.id,
#       Match.matchId
#   ).filter(
#       Match.gameVersion == max_game_version,
#       Match.replayDownloaded == True,
#       Match.sceneDownloaded == False
#   ).order_by(Match.playDatetime.desc()).all()
#
#   print(f'Found {len(matches)} matches')
#   for match in matches:
#     timeline = session.query(
#         MatchTimeline
#     ).filter(
#         MatchTimeline.matchId == match.matchId
#     ).scalar()
#
#     if timeline is None:
#       print(f"Timeline not found for {match.matchId}")
#       continue
#
#     clientApi.watchReplay('6946067565')
#     # clientApi.watchReplay(match.matchId.split('_')[1])
#     break
