import json

from pip._vendor import requests


class DiscordService:

  @staticmethod
  def send_discord_webhook(url, content):
    data = {
      "content": content
    }

    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
      result.raise_for_status()
    except requests.exceptions.HTTPError as err:
      print(err)
    else:
      print("Payload delivered successfully, code {}.".format(result.status_code))

