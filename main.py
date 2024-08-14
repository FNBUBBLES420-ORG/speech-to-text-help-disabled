import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import librosa
import numpy as np
from fuzzywuzzy import process
import nltk
from nltk.corpus import stopwords
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox, simpledialog

# Download NLTK data (only need to run once)
nltk.download('stopwords')

# Load the pre-trained Wav2Vec 2.0 model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Predefined phrases that the person might say
predefined_phrases = [
    "Hello, how are you?",
    "I need help with something",
    "Can you please assist me?",
    "What time is it?",
    "Thank you very much",
    "I'm feeling good today",
    "Where is the bathroom?",
    "I would like to eat something"
]

def pre_process_audio(audio_data):
    """Advanced audio pre-processing with noise reduction and compression."""
    y, sr = librosa.load(audio_data, sr=16000)
    y = librosa.effects.preemphasis(y)
    y = librosa.effects.trim(y)[0]
    y = librosa.effects.time_stretch(y, rate=1.1)
    return y, sr

def recognize_speech(audio_data):
    """Transcribe speech using Wav2Vec 2.0."""
    y, sr = pre_process_audio(audio_data)
    input_values = tokenizer(y, return_tensors="pt", padding="longest").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcript = tokenizer.batch_decode(predicted_ids)[0]
    return transcript.lower()

def match_phrase(transcript):
    """Match the recognized text with predefined phrases using contextual NLP."""
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in transcript.split() if word not in stop_words]
    cleaned_transcript = ' '.join(filtered_words)
    
    best_match = process.extractOne(cleaned_transcript, predefined_phrases)
    return best_match[0] if best_match[1] > 70 else transcript

def feedback_loop(recognized_text):
    """Sophisticated feedback loop with continuous learning."""
    feedback = messagebox.askquestion("Confirmation", f"Did you mean: '{recognized_text}'?")
    if feedback == 'no':
        correct_text = simpledialog.askstring("Correction", "Please enter the correct phrase:")
        if correct_text:
            predefined_phrases.append(correct_text)
        return correct_text
    return recognized_text

def start_recognition():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        audio_data = audio.get_wav_data()

        # Save the audio to a file
        with open("temp.wav", "wb") as f:
            f.write(audio_data)

        # Recognize speech
        transcript = recognize_speech("temp.wav")
        matched_phrase = match_phrase(transcript)
        final_output = feedback_loop(matched_phrase)
        
        messagebox.showinfo("Final Output", f"You said: {final_output}")

def create_gui():
    root = tk.Tk()
    root.title("Speech Recognition Assistant")
    root.geometry("300x200")

    start_button = tk.Button(root, text="Start Recognition", command=start_recognition, font=("Arial", 14))
    start_button.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
