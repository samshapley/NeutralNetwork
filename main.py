from youtube import YouTubeSearch

API_KEY = 'AIzaSyAUL3RG9_REUaKmb9L-q3MhHbFQgF9R_AI'
query = input("Enter your search query: ")

youtube_search = YouTubeSearch(API_KEY)

search_response = youtube_search.search_videos(query)

if search_response:
    youtube_search.save_json_to_file(search_response)
