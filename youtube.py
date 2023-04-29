from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ai import AI
from utils import load_prompts, parse_bullets
import openai
import pprint
import json

class YouTubeSearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.prompts = load_prompts()

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

    def save_json_to_file(self, query, search_response, filename='search_response.json'):
        # Read existing JSON file
        with open(filename, 'r') as f_in:
            json_data = json.load(f_in)

        # Update JSON file with new search results
        with open(filename, 'w') as f_out:
            # Create new search object to append to existing list
            search_object = {
                "query": query,
                "search_response": search_response
            }
            json_data['searches'].append(search_object)
            json.dump(json_data, f_out)

    def search_loop(self, query):
        # Call the search_videos function once with user-specified input
        search_response = self.search_videos(query)

        self.save_json_to_file(query, search_response)

        with open('search_response.json', 'r') as f:
            search_response = json.load(f)
            ai = AI(system=self.prompts["NEW_SEARCH"], openai_module=openai)
            prompt =  str(search_response)
            response, messages = ai.generate_response(prompt)
            
            # Parse response
            queries = parse_bullets(response)
            
            for query in queries:
                search_response = self.search_videos(query)
                self.save_json_to_file(query, search_response)

