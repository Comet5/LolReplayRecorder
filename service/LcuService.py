import os
import time
import subprocess
from os import times

import psutil
from sqlalchemy import or_, asc

import common.DbConnection as db
from api.LolClientApi import LolClientApi
from entity.MatchTimelineKillFrame import MatchTimelineKillFrame
from entity.Match import Match
from entity.Video import Video
from entity.Player import Player
from entity.PlayerAccount import PlayerAccount
import config


class LcuService:
  lcu = None

  def __init__(self):
    return

  def run_league_of_legends(self):
    self.modify_config_file()
    if not os.path.exists(config.LOL_EXE_PATH):
      print(f"League of Legends 실행 파일을 찾을 수 없습니다: {config.LOL_EXE_PATH}")
      return

    print("League of Legends를 실행합니다...")
    # subprocess.run(["open", config.LOL_EXE_PATH])
    self.lcu = LolClientApi()

  def modify_config_file(self):
    if not os.path.exists(config.LOL_CONFIG_PATH):
      print(f"설정 파일을 찾을 수 없습니다: {config.LOL_CONFIG_PATH}")
      return False

    with open(config.LOL_CONFIG_PATH, 'r', encoding='utf-8') as file:
      lines = file.readlines()

    # 수정할 설정 값
    modified_lines = []
    for line in lines:
      if line.startswith("WindowMode"):
        modified_lines.append("WindowMode=1\n")  # 윈도우 모드 활성화
      elif line.startswith("Width"):
        modified_lines.append("Width=1024\n")  # 해상도 너비 낮추기
      elif line.startswith("Height"):
        modified_lines.append("Height=768\n")  # 해상도 높이 낮추기
      else:
        modified_lines.append(line)

    # 파일에 수정된 내용을 다시 작성
    with open(config.LOL_CONFIG_PATH, 'w', encoding='utf-8') as file:
      file.writelines(modified_lines)

    print("설정 파일이 성공적으로 수정되었습니다.")
    return True

  def download_replay(self, target_nicknames: [], start_datetime):
    with (db.session() as session):
      players = session.query(Player).filter(
          Player.nickname.in_(target_nicknames)).all()
      for player in players:
        print(player.nickname)
        player_accounts = session.query(PlayerAccount).filter(
            PlayerAccount.playerId == player.id).all()
        for player_account in player_accounts:
          print(f'\t{player_account.summonerName} id: {player_account.id}')
          matches = session.query(Match).filter(
              Match.playerAccountId == player_account.id
          ).filter(
              Match.replayDownloaded == 0
          ).filter(
              Match.playDatetime >= start_datetime
          ).all()

          for match in matches:
            print(f'\t\t{match.matchId}')
            self.lcu.downloadReplay(match.matchId.split('_')[1])
            match.replayDownloaded = 1
            time.sleep(0.1)
      session.commit()

  def download_kill_scene(self, target_nicknames: [], start_datetime):
    with (db.session() as session):
      players = session.query(Player).filter(
          Player.nickname.in_(target_nicknames)).all()
      for player in players:
        print(f'player.nickname id: {player.id}')
        player_accounts = session.query(PlayerAccount).filter(
            PlayerAccount.playerId == player.id).all()
        for player_account in player_accounts:
          print(f'\t{player_account.summonerName} id: {player_account.id}')
          matches = session.query(Match).filter(
              Match.playerAccountId == player_account.id
          ).filter(
              Match.sceneDownloaded == 0
          ).filter(
              Match.playDatetime >= start_datetime
          ).filter(
              Match.queueId.in_([420])
          ).all()
          for match in matches:
            print(f'\t\t{match.matchId}')

            kill_frames = session.query(MatchTimelineKillFrame).filter(
                MatchTimelineKillFrame.matchId == match.matchId
            ).filter(
                or_(
                    MatchTimelineKillFrame.killerPlayerAccountId == player_account.id,
                    MatchTimelineKillFrame.assistPuuids.like(f'%{player_account.puuid}%')
                )
            ).all()
            if len(kill_frames) == 0:
              print(f'No kill frames found for {player_account.summonerName} {match.matchId}')
              continue

            self.kill_client()
            time.sleep(5)
            self.lcu.watchReplay(match.matchId)
            time.sleep(15)
            self.lcu.focusChampionByNickname(player_account.summonerName)
            time.sleep(3)
            self.lcu.focusChampionByNickname(player_account.summonerName)

            self.__record_frame(kill_frames, session)
            match.sceneDownloaded = 1


  def __record_frame(self, frames, session):
    categorized_frames = self.__categorize_frames(frames)
    for frames in categorized_frames:
      startSeconds = frames[0].eventTime/1000 - 10
      endSeconds = frames[len(frames)-1].eventTime/1000 + 5
      playSeconds = endSeconds - startSeconds
      print(f"len: {len(frames)} startSeconds: {startSeconds}, endSeconds: {endSeconds}, playSeconds: {playSeconds}")
      res = self.lcu.start_recording(startSeconds, endSeconds)
      video = Video(playSeconds=playSeconds, state='WAIT_VIDEO', localFileName=res['path'].rsplit('/', 1)[1])
      session.add(video)
      session.flush()
      for frame in frames:
        frame.videoId = video.id
        session.add(frame)
      time.sleep(playSeconds + 5)

  def __categorize_frames(self, frames):
    sorted_frames = sorted(frames, key=lambda frame: frame.eventTime)

    categories = []
    current_category = []
    last_event_time = None

    for frame in sorted_frames:
      print(frame.eventTime)
      if last_event_time is None or frame.eventTime - last_event_time < 10000:
        print('------------------------sooo')
        current_category.append(frame)
      else:
        categories.append(current_category)
        current_category = [frame]
      last_event_time = frame.eventTime
    if current_category:
      categories.append(current_category)

    return categories

  def run_replay(self, match_id):
    self.lcu.watchReplay(match_id)

  def kill_client(self):
    for proc in psutil.process_iter(['pid', 'name']):
      if proc.info['name'] == 'LeagueofLegends':
        try:
          proc.kill()
          print(f"Killed process {proc.info['name']} with PID {proc.info['pid']}")
        except psutil.NoSuchProcess:
          print("Process no longer exists.")
        except psutil.AccessDenied:
          print("Access denied to kill the process.")
        except Exception as e:
          print(f"Error: {e}")