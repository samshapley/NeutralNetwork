from pytube import YouTube
import os
import whisper

def transcribe_video(link):
    model = whisper.load_model("tiny")

    yt = YouTube(link, use_oauth=True)

    print("Downloading Audio")
    audio = yt.streams.get_audio_only()
    audio_file = "temp.mp3"
    audio.download(filename=audio_file)

    print("Transcribing Video")
    result = model.transcribe(audio_file)
    
    return result["text"]
