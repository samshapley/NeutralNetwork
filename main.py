from youtube import YouTubeSearch
import openai
from ai import AI

# Set up OpenAI API key
openai.api_key = "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"
youtube_api_key = 'AIzaSyBA43hoEQmwUEBynYWjQKsazVnRr6ybFb0'

youtube_search = YouTubeSearch(youtube_api_key)


query = input("Enter an Opinion: ")


youtube_search.search_loop(query)


# youtube_search.post_comment("mv4gQ7G-3RU", "Hello World")