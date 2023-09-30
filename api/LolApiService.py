import time

import requests
import config
from data import Riot
from data.enum.riot.RiotPlatform import RiotPlatform
from data.enum.riot.RiotRegion import RiotRegion


class RiotApiService:

    def __init__(self):
        pass

    def getSummonerByName(self, riotPlatform:RiotPlatform, nickname) -> Riot.Summoner:
        res = RiotApiService.__request(uri=f"https://{riotPlatform.riotId}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}")
        if res.status_code == 404:
            return None
        summoner = Riot.convertFromDict(Riot.Summoner, dict(res.json()))
        return summoner


    def getLeagueEntriesBySummonerId(self, riotRegion:RiotRegion, summonerId) -> [Riot.LeagueEntry]:
        res = RiotApiService.__request(uri=f"https://{riotRegion.value}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}")
        if res.status_code == 404:
            return None
        resJson = res.json()
        if len(resJson) == 0:
            return None
        leagueEntries = []
        for leagueEntry in resJson:
            leagueEntry = Riot.convertFromDict(Riot.LeagueEntry, dict(leagueEntry))
            leagueEntries.append(leagueEntry)
        return leagueEntries


    def getMatchIdsByPuuid(self, riotRegion:RiotRegion, puuid):
        res = RiotApiService.__request(uri=f"https://{riotRegion.value}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids")
        if res.status_code == 404:
            return None
        matchIds = res.json()
        return matchIds


    def getMatchById(self, riotPlatform:RiotPlatform, id) -> Riot.Summoner:
        res = RiotApiService.__request(uri=f"https://{riotPlatform.riotId}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}")
        if res.status_code == 404:
            return None
        match = Riot.convertFromDict(Riot.Match, dict(json))
        return match


    def __request(self, uri):
        res = requests.get(url=uri, headers={'X-Riot-Token': config.RIOT_TOKEN}, timeout=10)
        print(f'{res.status_code} {res.elapsed.total_seconds()}  {res.url}')
        if res.status_code == 429:
            print('API_LIMIT :: Sleep10s')
            time.sleep(10)
            return RiotApiService.__request(uri)
        return res
