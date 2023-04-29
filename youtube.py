from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ai import AI
from utils import load_prompts, parse_bullets
import openai
import pprint
import json
from transcribe import transcribe_video
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class YouTubeSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.prompts = load_prompts()

    def search_videos(self, query, max_results=2):
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

    def get_video_comments(self, video_id, max_results=100):
        try:
            comments = []
            results = self.youtube.commentThreads().list(
                part='id,snippet',
                videoId=video_id,
                maxResults=max_results,
                textFormat='plainText',
                order = 'relevance'
            ).execute()

            for item in results['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append({
                    'author': comment['authorDisplayName'],
                    'text': comment['textOriginal'],
                    'likes': comment['likeCount'],
                    'published_at': comment['publishedAt']
                })

            return comments

        except HttpError as e:
            print(f'An error occurred: {e}')
            return None

    def video_json(self, query, search_response):

        # Update JSON file with new search result
        searches = []
        # Create new search object to append to existing list
        for item in search_response:

            video_id = item['id']['videoId']
            link = f'https://www.youtube.com/watch?v={video_id}'
            transcript = transcribe_video(link)

            search_object = {
                "query": query,
                "search_response": item,
                "transcript": transcript
            }

            searches.append(search_object)

        json_data = {'searches': searches}
 
        return json_data
            
    def search_loop(self, query):
        # Call the search_videos function once with user-specified input
        search_response = self.search_videos(query)["items"]
        videos_json = self.video_json(query, search_response)

        user_opinion = "User Opinion: " + query

        # open search_response.json
        with open('search_response.json', 'r') as f:
            videos_json = json.load(f)

        for video in videos_json['searches']:
            print("Initializing AI...")
            ai = AI(system=self.prompts["SENTIMENT"], openai_module=openai)
            print("Generating response...")
            response, messages = ai.generate_response(f"{video} \n {user_opinion}")

            print(response)

        # with open('search_response.json', 'r') as f:
        #     search_response = json.load(f)
        #     print(search_response)
        #     del search_response['searches'][0]['transcript']

        #     ai = AI(system=self.prompts["NEW_SEARCH"], openai_module=openai)
        #     prompt =  str(search_response)
        #     
            
        #     # Parse response
        #     queries = parse_bullets(response)
            
        #     for query in queries:
        #         search_response = self.search_videos(query)
                # self.save_json_to_file(query, search_response)

    @staticmethod
    def post_comment(video_id, comment):
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

        def main():
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

            api_service_name = "youtube"
            api_version = "v3"
            client_secrets_file = "client_secret.json"

            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials = flow.run_console()
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, credentials=credentials)

            request = youtube.commentThreads().insert(
                part="snippet",
                body={
                  "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                      "snippet": {
                        "textOriginal": comment
                      }
                    }
                  }
                }
            )
            response = request.execute()

            print(response)

        main()






