from textblob import TextBlob
import random
from emoji_map import emoji_dict

def get_emotion_from_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return "excited"
    elif polarity > 0.2:
        return "happy"
    elif polarity < -0.5:
        return "angry"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"

def get_emojis(emotion):
    return random.sample(emoji_dict.get(emotion, ["🤔"]), 2)

import gradio as gr

def predict_emojis(text):
    emotion = get_emotion_from_text(text)
    emojis = get_emojis(emotion)
    return f"Emotion: {emotion}\nEmojis: {' '.join(emojis)}"

iface = gr.Interface(
    fn=predict_emojis,
    inputs=gr.Textbox(lines=2, placeholder="Write something here..."),
    outputs="text",
    title="AI Emoji Generator",
    description="Write a sentence and get the corresponding emojis based on detected emotion."
)

if __name__ == "__main__":
    iface.launch()
