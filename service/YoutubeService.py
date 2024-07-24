import os

import googleapiclient
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


class YoutubeService:

    def __init__(self):
        CLIENT_SECRETS_FILE = "service/client_secret_851182046740-b6pndvfilir7id9edv13os6p5dd1o6s7.apps.googleusercontent.com.json"
        SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

        # flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        # flow._OOB_REDIRECT_URI = "http://127.0.0.1:8080"
        # credentials = flow.run_local_server(port=0)
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
        flow.redirect_uri = "https://www.epromatch.com"
        auth_url, __ = flow.authorization_url(prompt="consent")
        print('Please go to this URL: {}'.format(auth_url))
        # code = input('Enter the authorization code: ')
        code = "4/0AcvDMrCfahTTyxDvsgym15ZmmYpHs4--Ix9PdV2U4q7jJfH89iT0uzL_w-7SWNgjkuj1Ig"
        flow.fetch_token(code=code)
        self.client = googleapiclient.discovery.build(
            "youtube", "v3", credentials=flow.credentials
        )

        # self.client = build('youtube', 'v3', credentials=credentials)

    def upload_video(self, video_file, title, description, category, tags):
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags,
                'categoryId': category
            },
            'status': {
                'privacyStatus': 'public',  # Options: 'public', 'private', 'unlisted'
            }
        }

        media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

        request = self.client.videos().insert(
            part='snippet,status',
            body=body,
            media_body=media
        )

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f'Uploaded {int(status.progress() * 100)}%')

        print(f'Video uploaded successfully: https://www.youtube.com/watch?v={response["id"]}')
