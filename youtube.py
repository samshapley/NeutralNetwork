from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ai import AI
from utils import load_prompts, parse_bullets
import openai
import pprint
import json
from transcribe import transcribe_video

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

    def save_json_to_file(self, query, search_response, filename='search_response.json'):

        # Update JSON file with new search results
        with open(filename, 'w') as f_out:

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

            # Write the JSON data to the file
            with open(filename, 'w') as f_out:
                json.dump(json_data, f_out, indent=4)

    def search_loop(self, query):
        # Call the search_videos function once with user-specified input
        search_response = self.search_videos(query)["items"]

        self.save_json_to_file(query, search_response)

        # with open('search_response.json', 'r') as f:
        #     search_response = json.load(f)
        #     print(search_response)
        #     del search_response['searches'][0]['transcript']

        #     ai = AI(system=self.prompts["NEW_SEARCH"], openai_module=openai)
        #     prompt =  str(search_response)
        #     response, messages = ai.generate_response(prompt)
            
        #     # Parse response
        #     queries = parse_bullets(response)
            
        #     for query in queries:
        #         search_response = self.search_videos(query)
        #         self.save_json_to_file(query, search_response)

