## LICENSE
## This project is proprietary and all rights are reserved by the author.
## Unauthorized copying, distribution, or modification of this project is strictly prohibited.
## Unless You have written permission from the Developer or the FNBUBBLES420 ORG.

import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import threading
import queue
from config import (APPEARANCE_MODE, THEME_COLOR, FONT,
                    AMBIENT_NOISE_ADJUSTMENT_DURATION, TIMEOUT_DURATION, PHRASE_TIME_LIMIT)

class SpeechToTextApp:
    def __init__(self, master):
        self.master = master
        master.title("TEAMFNB420 - Speech to Text for OBS")

        # Configure the main window using settings from config.py
        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(THEME_COLOR)
        self.master.geometry('500x300')  # Directly set the window size here
        self.master.resizable(False, False)

        # Queue for thread-safe GUI updates
        self.queue = queue.Queue()

        # Text area to display the transcription
        self.text_area = scrolledtext.ScrolledText(master, wrap='word', width=50, height=10, font=FONT)
        self.text_area.pack(pady=20, padx=20)
        self.text_area.config(state='disabled')

        # Start/Stop button
        self.toggle_btn = ctk.CTkButton(master, text="Start Listening", command=self.toggle_listening, corner_radius=10)
        self.toggle_btn.pack()

        # Close button
        self.close_btn = ctk.CTkButton(master, text="Close", command=self.close_application, corner_radius=10)
        self.close_btn.pack(pady=10)

        # Speech Recognizer and Microphone
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False

        # Start a thread to process queue items
        self.process_queue()

    def toggle_listening(self):
        if self.listening:
            self.listening = False
            self.toggle_btn.configure(text="Start Listening")
        else:
            self.listening = True
            self.toggle_btn.configure(text="Stop Listening")
            threading.Thread(target=self.listen_and_transcribe, daemon=True).start()

    def listen_and_transcribe(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=AMBIENT_NOISE_ADJUSTMENT_DURATION)
            self.queue.put("Listening...")
            while self.listening:
                try:
                    audio = self.recognizer.listen(source, timeout=TIMEOUT_DURATION, phrase_time_limit=PHRASE_TIME_LIMIT)
                    text = self.recognizer.recognize_google(audio)
                    self.queue.put(text)
                    with open("transcription.txt", "a") as file:
                        file.write(text + "\n")
                except sr.WaitTimeoutError:
                    self.queue.put("No speech detected, try speaking again...")
                except sr.UnknownValueError:
                    self.queue.put("Could not understand audio")
                except sr.RequestError as e:
                    self.queue.put(f"Request failed; {e}")

    def process_queue(self):
        try:
            message = self.queue.get_nowait()
            self.update_text(message)
        except queue.Empty:
            pass
        finally:
            self.master.after(100, self.process_queue)

    def update_text(self, message):
        self.text_area.config(state='normal')
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, message)
        self.text_area.config(state='disabled')

    def close_application(self):
        """Close the application window."""
        self.master.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = SpeechToTextApp(root)
    root.mainloop()
    
# The main.py file contains the main code for the SpeechToTextApp class. The class initializes the application window, configures the GUI, and sets up the speech recognition functionality. It includes methods for starting and stopping the speech recognition process, listening for audio input, and updating the GUI with transcribed text.

# The main.py file also includes the necessary imports for customtkinter, tkinter, speech_recognition, threading, and queue, as well as the configuration settings from config.py.

# The SpeechToTextApp class includes methods for toggling listening mode, listening for audio input, processing the queue for GUI updates, updating the text area with transcribed text, and closing the application window.

# Finally, the main.py file creates an instance of the SpeechToTextApp class and runs the application using the customtkinter library. The application window is displayed, and the user can interact with the speech-to-text functionality. When the user closes the application window, the application terminates
