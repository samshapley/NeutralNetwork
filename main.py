from youtube import YouTubeSearch
import openai
from ai import AI

# Set up OpenAI API key
openai.api_key = "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"
youtube_api_key = 'AIzaSyBA43hoEQmwUEBynYWjQKsazVnRr6ybFb0'


# query = input("Enter your search query: ")

youtube_search = YouTubeSearch(youtube_api_key)

# # search_response = youtube_search.search_videos(query)
# youtube_search.search_loop(query)

# # if search_response:
# #     youtube_search.save_json_to_file(search_response)
# # Get the video ID from the search response

youtube_search.post_comment("mv4gQ7G-3RU", "Hello World")