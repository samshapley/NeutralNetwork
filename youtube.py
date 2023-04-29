from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pprint
import json

class YouTubeSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search_videos(self, query, max_results=10):
        try:
            search_response = self.youtube.search().list(
                q=query,
                part='id,snippet',
                maxResults=max_results
            ).execute()

            return search_response

        except HttpError as e:
            print(f'An error occurred: {e}')
            return None

    def save_json_to_file(self, search_response, filename='search_response.json'):
        with open(filename, 'w') as f:
            json.dump(search_response, f)
