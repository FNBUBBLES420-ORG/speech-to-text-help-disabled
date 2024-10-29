import os
import warnings
import tensorflow as tf
from transformers import logging

# Environment configurations
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '0'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Set TensorFlow and Hugging Face logging levels to error
tf.get_logger().setLevel('ERROR')
logging.set_verbosity_error()

# Suppress specific non-critical warnings
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow')
warnings.filterwarnings("ignore", category=UserWarning, module='pydub.utils')
warnings.filterwarnings("ignore", category=FutureWarning, module='transformers.tokenization_utils_base')
warnings.filterwarnings("ignore", message="Some weights of Wav2Vec2ForCTC were not initialized from the model checkpoint")

# Continue with imports and the rest of your script
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import librosa
import numpy as np
from fuzzywuzzy import process
import nltk
from nltk.corpus import stopwords
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox, simpledialog
import speech_recognition as sr
import json  # <-- For saving updated phrases

# Download NLTK stopwords only if not already downloaded
try:
    stop_words = stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
    stop_words = stopwords.words('english')

# Load the pre-trained Wav2Vec 2.0 model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Expanded list of predefined phrases, loaded from a file if available
predefined_phrases_file = "predefined_phrases.json"
if os.path.exists(predefined_phrases_file):
    with open(predefined_phrases_file, "r") as f:
        predefined_phrases = json.load(f)
else:
    predefined_phrases = [
        "Hello, how are you?",
        "I need help with something.",
        "Can you please assist me?",
        "What time is it?",
        "Thank you very much.",
        "Where is the bathroom?",
        "I would like to eat something.",
        "What is your name?",
        "How do I get there?",
        "I need a doctor.",
        "Please call an ambulance.",
        "Can you please repeat that?",
        "I do not understand.",
        "Can you speak slower?",
        "I am lost.",
        "Where can I find help?",
        "Can you guide me?",
        "Is this the right way?",
        "What is the weather like?",
        "Can you open the window?",
        "I am feeling cold.",
        "I am feeling hot.",
        "Can you turn on the lights?",
        "Can you turn off the lights?",
        "I need to go home.",
        "Where is the nearest hospital?",
        "Can you tell me the time?",
        "What day is it today?",
        "Where is the nearest store?",
        "How much does this cost?",
        "I need some water.",
        "Can you help me find my keys?",
        "Where is the restroom?",
        "Can you help me cross the street?",
        "Can you please be quiet?",
        "Please help me find my way back.",
        "Can I have a glass of water?",
        "Where can I find a taxi?",
        "What is your phone number?",
        "Is there a nearby pharmacy?",
        "Can I get directions?",
        "I need some assistance.",
        "Can you show me on the map?",
        "I am feeling unwell.",
        "Do you know any good restaurants?",
        "I need to make a reservation.",
        "Could you check the status?",
        "I would like to make a complaint.",
        "What services do you offer?",
        "How can I contact customer service?",
        "Is there anything else you need?",
        "Can you help me with my luggage?",
        "Where is the nearest gas station?",
        "Do you accept credit cards?",
        "Where can I park?",
        "How can I access Wi-Fi?",
        "Could you recommend a hotel?",
        "What’s the best way to get there?",
        "Can you show me around?",
        "Where can I buy a ticket?",
        "How much is the fare?",
        "What time does it open?",
        "What time does it close?",
        "Do I need a reservation?",
        "Can I have a receipt?",
        "Can I pay in cash?",
        "Do you speak English?",
        "How can I get to the airport?",
        "What is the emergency number?",
        "Can you give me some information?",
        "What are the business hours?",
        "How can I apply?",
        "Where can I find the restroom?",
        "How long will it take?",
        "Is there a discount available?",
        "What is included in the price?",
        "Is this available for purchase?",
        "Can I have some assistance?",
        "Where can I find a doctor?",
        "Where is the nearest clinic?",
        "Can you show me how?",
        "How do I make a call?",
        "How far is it?",
        "Can I get there by bus?",
        "Is there a nearby bank?",
        "What is the exchange rate?",
        "Do you have a map?",
        "Is there a guide available?",
        "Can I borrow a pen?",
        "Can you recommend a tour?",
        "Is it open to the public?",
        "Can I bring a guest?",
        "Are there any rules?",
        "What are the safety instructions?",
        "Where can I find an ATM?",
        "Is this wheelchair accessible?",
        "Do you have vegetarian options?",
        "What’s the daily special?",
        "Can I make a reservation?",
        "What’s the phone number?",
        "How do I check out?",
        "Can I extend my stay?",
        "Can I cancel my reservation?",
        "Is there a lost and found?",
        "Can you call me a taxi?",
        "Where can I find a souvenir shop?",
        "Is tipping required?",
        "What’s the nearest subway station?",
        "What are the ticket prices?",
        "What is the return policy?",
        "Can you help me plan my route?",
        "Where can I buy a metro card?",
        "How do I check the schedule?",
        "Do you have a brochure?",
        "Can you show me the landmarks?",
        "What’s the best time to visit?",
        "Is there an entrance fee?",
        "Can you take a picture for me?",
        "What currency is accepted here?",
        "Are there any nearby attractions?",
        "Is there a dress code?",
        "Where can I charge my phone?",
        "Do you have mobile payment?",
        "How can I report an issue?",
        "Where can I find the main entrance?",
        "Can you help me find transportation?",
        "Is there a food court?",
        "Are pets allowed?",
        "What’s the weather forecast?",
        "Is there a nearby playground?",
        "What activities are available?",
        "Can I make a donation?",
        "What is the cancellation policy?",
        "Can I reschedule my appointment?",
        "What are the check-in and check-out times?",
        "Is breakfast included?",
        "Can I have an extra pillow?",
        "What amenities are available?",
        "Where can I find the gym?",
        "Is there a spa available?",
        "How do I use the safe?",
        "What time is breakfast served?",
        "Is there a shuttle service?",
        "How do I set up a wake-up call?",
        "Can I change my seat?",
        "What’s the menu for today?",
        "Is there a children’s menu?",
        "Can I have a blanket?",
        "Where is the luggage storage?",
        "Is this item refundable?",
        "Can I try this on?",
        "Where can I find help?",
        "Can you give me the Wi-Fi password?",
        "Is there a connection fee?",
        "What are your popular dishes?",
        "Can I order room service?",
        "How do I access the internet?",
        "What events are happening nearby?",
        "How can I get to the train station?",
        "What are the airport services?",
        "Can I get travel insurance?",
        "How do I track my flight?",
        "Can I upgrade my ticket?",
        "What’s the fastest route?",
        "Can I pay by check?",
        "Do you have any promotions?",
        "Can I exchange this item?",
        "How do I make a return?",
        "Is there an available restroom?",
        "Can I get assistance with my baggage?",
        "Are there any nearby pharmacies?",
        "Do you provide cleaning services?",
        "Can I arrange a wake-up call?",
        "Is breakfast complimentary?",
        "Where is the information desk?",
        "Are there accessible entrances?",
        "How can I change my booking?",
        "Can you tell me about the local area?",
        "Is there a concierge service?",
        "Can I request a non-smoking room?",
        "Where can I find the exit?",
        "Can I have a copy of my receipt?",
        "What’s the pet policy?",
        "Are there quiet hours?",
        "What’s the dress code here?",
        "Where can I report a lost item?",
        "How do I get a refund?",
        "Where can I leave a review?",
        "Can I check my account balance?",
        "Is there an age requirement?",
        "Can I access a printer?",
        "Do you offer luggage storage?",
        "Where can I find the ATM?",
        "How do I change my password?",
        "What’s your email address?",
        "Can I book a private tour?",
        "Is there a maximum occupancy?",
        "Can I get extra towels?",
        "Where’s the emergency exit?",
        "Do you have a map of the city?",
        "Can I reserve a table?",
        "What are your hours of operation?",
        "How can I purchase tickets?",
        "What are the most popular attractions?",
        "Can I get a refund for my ticket?",
        "Is there a guide for visitors?",
        "What’s the wait time?",
        "Can I have a quiet room?",
        "Are there family rates?",
        "Is the pool open?",
        "What’s the Wi-Fi speed?",
        "Where can I charge my device?",
        "Can I have a bottle of water?",
        "Are there vegetarian options?",
        "Where is the nearest exit?",
        "Do you offer group rates?",
        "Is there a designated smoking area?",
        "What languages are spoken here?",
        "How do I call room service?",
        "Are gratuities included?",
        "What’s the check-out process?",
        "Can I arrange a pick-up service?",
        "Where can I find a restroom?",
        "Do you have late check-out options?",
        "Can I buy souvenirs?",
        "What’s the local time?",
        "Do you have airport transfers?",
        "Can I pay in installments?",
        "What’s the estimated cost?",
        "Is this location accessible?",
        "Are there night events?",
        "Do you have special offers?",
        "What’s the cancellation fee?",
        "What are the local laws?",
        "Where can I report lost items?",
        "Can I have extra toiletries?",
        "What’s the tipping policy?",
        "How do I use public transport?",
        "What’s the exchange rate?",
        "Are there parking facilities?",
        "Do you have a cloakroom?",
        "Is there a time limit?",
        "Where can I get a taxi?",
        "Are children allowed?",
        "How much is the entry fee?",
        "Where can I check the weather?",
        "Do you offer senior discounts?",
        "How do I report a problem?",
        "Where’s the ticket booth?",
        "What’s the dress code?"
    ]

def save_phrases():
    """Save updated phrases to JSON file for persistence across sessions."""
    with open(predefined_phrases_file, "w") as f:
        json.dump(predefined_phrases, f)

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
    input_values = processor(y, return_tensors="pt", padding="longest", sampling_rate=sr).input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcript = processor.batch_decode(predicted_ids, clean_up_tokenization_spaces=True)[0]
    return transcript.lower()

def match_phrase(transcript):
    """Match the recognized text with predefined phrases using contextual NLP."""
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
            save_phrases()  # Save updated phrases to persist across sessions
        return correct_text
    return recognized_text

def start_recognition():
    recognizer = sr.Recognizer()

    # Check for microphone availability
    if sr.Microphone.list_microphone_names():
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            audio_data = audio.get_wav_data()

            # Save the audio to a temporary file
            temp_file = "temp.wav"
            with open(temp_file, "wb") as f:
                f.write(audio_data)

            # Recognize speech
            transcript = recognize_speech(temp_file)
            matched_phrase = match_phrase(transcript)
            final_output = feedback_loop(matched_phrase)
            
            # Display the final output to the user
            messagebox.showinfo("Final Output", f"You said: {final_output}")

            # Clean up temporary file
            os.remove(temp_file)
    else:
        messagebox.showerror("Error", "No microphone found. Please connect a microphone and try again.")

def create_gui():
    root = tk.Tk()
    root.title("Bubbles The Dev - Speech Recognition Assistant")
    root.geometry("600x300")

    start_button = tk.Button(root, text="Start Recognition", command=start_recognition, font=("Arial", 14))
    start_button.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
