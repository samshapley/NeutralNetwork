from youtube import YouTubeSearch
import openai
from ai import AI

# Set up OpenAI API key
openai.api_key = "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"
youtube_api_key = 'AIzaSyAUL3RG9_REUaKmb9L-q3MhHbFQgF9R_AI'


query = input("Enter your search query: ")

youtube_search = YouTubeSearch(youtube_api_key)

search_response = youtube_search.search_videos(query)

if search_response:
    youtube_search.save_json_to_file(search_response)

# ai = AI(system="You answer questions whihc are jumbled up",openai_module=openai)
# response, messages = ai.generate_response("MSYDNYEATDEHNOADIGHSNAIWROUTUAY", voice=False)