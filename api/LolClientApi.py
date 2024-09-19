import os
import subprocess
import time

import requests, json

from lcuapi import LCU, Event, EventProcessor
import config


class LolClientApi:
  host = "https://127.0.0.1:2999"

  def __init__(self):
    self.__initLcu()
    # print(self.lcuPort)
    # print(self.lcuPw)

  def __initLcu(self):
    self.lcu = LCU()
    self.lcu.attach_event_processor(PrintSomeEventInfo())
    self.lcu.wait_for_client_to_open()
    self.lcu.wait_for_login()


    # gameId = "6571041847"
    #
    # finished = self.lcu.get(f'/lol-replays/v1/configuration')
    # print("Has the client finished it's starting up?", finished)
    #
    # finished = self.lcu.get(f'/lol-replays/v1/metadata/{gameId}')
    # print("Has the client finished it's starting up?", finished)
    #
    # finished = self.lcu.post(f'/lol-replays/v1/rofls/{gameId}/download', {"contextData": "string"})
    # print(finished.reason)
    # print("Has the client finished it's starting up?", finished)
    # print(finished.text)
    # with open("C:/Program Files/Riot Games/League of Legends/lockfile", 'r') as f:
    #   data = f.read().split(":")
    #   self.lcuPort = data[2]
    #   self.lcuPw = data[3]

  def getEvents(self):
    return self.getAllGameData()['events']['Events']

  def getAllGameData(self):
    json = self.__get("/liveclientdata/allgamedata")
    return json


  def downloadReplay(self, gameId):
    json = self.lcu.post(f"/lol-replays/v1/rofls/{gameId}/download", {"contextData": "string"})
    return json

  def watchReplay(self, gameId):
    if os.path.exists(config.LOL_INGAME_EXE_PATH) == False:
      print("League of Legends.exe file not found")
      return
    json = self.lcu.post(f"/lol-replays/v1/rofls/{gameId}/watch", {"contextData": "string"})
    # json = self.lcu.post(f"/lol-replays/v2/metadata/{gameId}/create", {"contextData": "string"})

    # time.sleep(3)
    # # windows
    # subprocess.run(["open", f'"{config.LOL_EXE_PATH}" "{config.LOL_REPLAY_DIR_PATH}KR-{gameId}.rofl"'])

    # mac
    # print("open", "-na", f"{config.LOL_INGAME_EXE_PATH}", "--args", f"{config.LOL_REPLAY_DIR_PATH}KR-{gameId}.rofl")
    # subprocess.run(["open", "-na", f"{config.LOL_INGAME_EXE_PATH}", "--args", f"{config.LOL_REPLAY_DIR_PATH}KR-{gameId}.rofl"], check=True)


    # if os.path.exists(config.LOL_CONFIG_DIR_PATH+"LeagueClientSettings.yaml") == False:
    #   print("LeagueClientSettings.yaml file not found")
    #   return
    # if os.path.exists(config.LOL_EXE_PATH) == False:
    #   print("League of Legends.exe file not found")
    #   return
    #
    # # Find the locale in the LeagueClientSettings.yaml file
    # with open(config.LOL_CONFIG_DIR_PATH+"LeagueClientSettings.yaml", "r") as file:
    #   for line in file:
    #     if "locale: " in line:
    #       locale = line.split(": ")[1].strip()
    #
    # command = f'@start "" "{config.LOL_EXE_PATH}" "spectator spectate-record-kr.op.gg:80 wfDgI4LbMIoYvUebzWe4wthfPgJUbrVg {gameId} KR" "-UseRads" "-Locale={locale}" "-GameBaseDir=.."'
    #
    # # Use subprocess to execute the command
    # subprocess.call(command, shell=True)
    # time.sleep(5)

    # # Check if the path exists
    # if os.path.exists(os.path.join(rads_path, "Game")):
    #   # Change the working directory
    #   os.chdir(os.path.join(rads_path, "Config"))
    #
    #   # Find the locale in the LeagueClientSettings.yaml file
    #   with open("LeagueClientSettings.yaml", "r") as file:
    #     for line in file:
    #       if "locale: " in line:
    #         locale = line.split(": ")[1].strip()
    #
    #   # Change the RADS_PATH
    #   rads_path = os.path.join(rads_path, "Game")
    #
    #   # Change the working directory
    #   os.chdir(rads_path)
    #
    #   # Check if the League of Legends.exe exists
    #   if os.path.exists("League of Legends.exe"):
    #     # Define the command as a string
    #     command = f'@start "" "League of Legends.exe" "spectator spectate-record-kr.op.gg:80 wfDgI4LbMIoYvUebzWe4wthfPgJUbrVg {gameId} KR" "-UseRads" "-Locale={locale}" "-GameBaseDir=.."'
    #
    #     # Use subprocess to execute the command
    #     subprocess.call(command, shell=True)
    #     time.sleep(5)

    return json

  def moveTime(self, second:int):
    json = self.__post("/replay/playback", {"time": second})

  def focusChampionByNickname(self, nickname:str):
    json = self.__post("/replay/render",
   {
      "cameraAttached": "true",
      "cameraMode": "fps",
      "selectionName": nickname,
      "selectionOffset": {
        "x": 0.0,
        "y": 1911.85,
        "z": -1200.0
      }
    })

  def __get(self, uri:str):
    print("GET ::", f"{self.host, uri}")
    request = requests.get(f"{self.host}{uri}", verify=False)
    return request.json()

  def __post(self, uri:str, body=None):
    if body is None:
      body = {}
    print("POST ::", f"{self.host, uri}")
    headers = {'Content-Type': 'application/json;'}
    request = requests.post(f"{self.host}{uri}", json.dumps(body), headers=headers, verify=False)
    return request.json()


class PrintSomeEventInfo(EventProcessor):

  # The "can_handle" method must return True and False.
  # Return True if this event handler can handle the event. Return False if not.
  def can_handle(self, event: Event):
    if issubclass(event.__class__, Event):
      return True
    else:
      return False

  # The "handle" method defines the functionality of the handler.
  # This is where you write code to do something with the event.
  # In this example, I simply print out the URI of the event and the time at which it was created.
  # The only other attribute of an Event is: "event.data".
  def handle(self, event: Event):
    print(f"Event<uri={event.uri} created={event.created}>")