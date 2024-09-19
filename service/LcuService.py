import os
import time
import subprocess

import common.DbConnection as db
from api.LolClientApi import LolClientApi
from entity.Match import Match
from entity.MatchVideo import MatchVideo
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

  def download_replay(self, start_datetime):
    targetNicknames = ['Chovy', 'Peyz', 'Kiin', 'Canyon', 'Faker', 'ShowMaker',
                       'Zeus', 'Oner', 'Gumayusi', 'Keria']

    with (db.session() as session):
      players = session.query(Player).filter(
          Player.nickname.in_(targetNicknames)).all()
      for player in players:
        print(player.nickname)
        player_accounts = session.query(PlayerAccount).filter(
            PlayerAccount.playerId == player.id).all()
        for player_account in player_accounts:
          print(f'\t{player_account.summonerName}')
          matches = session.query(Match).outerjoin(
              MatchVideo, Match.matchId == MatchVideo.matchId
          ).filter(
              MatchVideo.matchId == None
              # Filter where MatchVideo does not exist
          ).filter(
              Match.playerAccountId == player_account.id
          ).filter(
              Match.replayDownloaded == 0
          ).filter(
              Match.playDatetime >= start_datetime
          ).all()

          for match in matches:
            self.lcu.downloadReplay(match.matchId.split('_')[1])
            match.replayDownloaded = 1
            time.sleep(0.1)
      session.commit()

  def run_replay(self, match_id):
    self.lcu.watchReplay(match_id)
