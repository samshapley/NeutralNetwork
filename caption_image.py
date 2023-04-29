from transformers import pipeline
from PIL import Image

def generate_caption(image_path):
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    image = Image.open(image_path)
    caption = image_to_text(image)[0]["generated_text"]
    return caption