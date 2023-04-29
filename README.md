# Neutral Network

This is a YouTube Comment Bot that utilizes OpenAI's GPT-4 model to generate and post comments on YouTube videos based on a user's opinion. The bot can also perform searches and extract video comments.

## Dependencies

- googleapiclient
- google-auth-oauthlib
- googleapiclient.errors
- openai
- pytube
- whisper
- transformers
- PIL (Pillow)

## Files

### youtube.py

This file contains the `YouTubeSearch` class, which is responsible for performing YouTube video searches, extracting video comments, and posting generated comments to YouTube. It also handles creating and updating a JSON file containing video search results and transcriptions.

### ai.py

This file contains the `AI` class, which interacts with the OpenAI GPT-4 model to generate comments or search queries based on the given prompts and context.

### utils.py

This file contains utility functions such as `load_prompts()` and `parse_bullets()` that assist in reading data from text files and parsing information.

### transcribe.py

This file contains the `transcribe_video()` function that downloads and transcribes the audio from a YouTube video using the Whisper ASR model.

### caption_image.py

This file contains the `generate_caption()` function, which utilizes the Hugging Face Transformers library to generate captions for images using the VIT-GPT2 model.

### prompt.py

This file contains the `get_code_from_file()` function that reads and returns the content of a Python file. It also creates a 'code.txt' file containing the codebase in a readable format.

### main.py

This file is the entry point of the application, where the user provides their opinion and the bot starts interacting with YouTube videos.

## Usage

1. Install the required dependencies.
2. Set up the API keys for OpenAI and YouTube in the `main.py` file.
3. Run `main.py` and input your opinion when prompted.
4. The bot will perform searches, generate comments, and interact with YouTube videos based on the given opinion.

Note: This codebase is meant for educational purposes and should not be used to manipulate or influence opinions on social media platforms.
