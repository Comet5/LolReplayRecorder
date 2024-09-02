import os
import time
import datetime


from api.LolClientApi import LolClientApi
import common.DbConnection as db
from entity.LolVersion import LolVersion
from entity.Match import Match
from entity.MatchVideo import MatchVideo
from entity.Player import Player
from entity.PlayerAccount import PlayerAccount

class ReplayService:
    def __init__(self):
        return

    def download_replay(self, start_datetime):
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
                Match.playDatetime >= start_datetime
            ).all()

            for match in matches:
              clientApi.downloadReplay(match.matchId.split('_')[1])
              match.replayDownloaded = 1
              time.sleep(0.1)
        session.commit()

    def get_replay_list(self):
        return os.listdir(self.replay_path)