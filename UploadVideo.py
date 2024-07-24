import os
from googleapiclient.errors import HttpError
from service.YoutubeService import YoutubeService

youtube_service = YoutubeService()
video_file = os.path.expanduser('~/Downloads/malloc.mp4')
title = 'malloc'
description = 'malloc'
category = '22'  # See https://developers.google.com/youtube/v3/docs/videoCategories/list
tags = ['tag1', 'tag2']

try:
  youtube_service.upload_video(video_file, title, description, category, tags)
except HttpError as e:
  print(f'An HTTP error {e.resp.status} occurred: {e.content}')