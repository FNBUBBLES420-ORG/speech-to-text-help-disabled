# Speech Recognition Assistant

## Overview

The Speech Recognition Assistant is a Python-based tool designed to help individuals with speech difficulties convert their spoken words into text. This tool leverages advanced speech recognition models, audio processing, and natural language processing techniques to provide accurate and contextually appropriate text output. It includes a user-friendly GUI built with Tkinter.

[FNBubbles420 ORG on github](https://github.com/FNBUBBLES420-ORG/readme.md)

## Features

- **Deep Learning with Wav2Vec 2.0**: Utilizes Facebook's Wav2Vec 2.0 model for robust and adaptable speech recognition.
- **Advanced Audio Pre-processing**: Includes noise reduction, dynamic range compression, and time stretching for better clarity.
- **Contextual Phrase Matching**: Implements Natural Language Processing (NLP) to match recognized speech with predefined phrases.
- **Continuous Learning**: Includes a feedback loop where the system learns from user corrections, improving over time.
- **User-Friendly GUI**: A simple graphical user interface (GUI) built with Tkinter makes the application easy to use.

## Requirements

Before running the application, ensure you have the following dependencies installed:

```
pip install torch transformers pydub librosa fuzzywuzzy nltk soundfile tk
```
- Alternatively, you can use the provided requirements.bat script to install these packages separately.

## How to Use

1. **Run the Application:**
- Execute the `main.py` script to launch the GUI.
- The application will display a window with a "Start Recognition" button.

2. **Start Speech Recognition:**
- Click the "Start Recognition" button.
- The application will listen to your speech and attempt to convert it to text.

3. **Feedback and Correction:**
- The application will display the recognized text and ask if it's correct.
- If the text is incorrect, you can provide the correct phrase, which the system will learn and remember for future use.

4. **View Final Output:**
- After processing and possible correction, the final recognized text will be displayed in a message box.

## Customization

- **Predefined Phrases:** You can edit or add to the `predefined_phrases` list in the script to match the most common phrases the user might say.
- **Model Training:** While the script uses a pre-trained model, you can replace it with a custom-trained model if necessary.

## Contribution

- Feel free to fork this repository, make improvements, and submit pull requests. Your contributions are welcome!

## Acknowledgements

- **[Facebook AI](https://github.com/pytorch/fairseq)**: For the Wav2Vec 2.0 model.
- **[NLTK](https://www.nltk.org/)**: For providing NLP tools.
- **[Librosa](https://librosa.org/)**: For audio processing.
- **[Pydub](https://github.com/jiaaro/pydub)**: For simple and easy audio manipulation.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: For the GUI framework.
- **[FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)**: For string matching and scoring.
- **[SoundFile](https://pysoundfile.readthedocs.io/en/latest/)**: For reading and writing sound files.
- **[Hugging Face Transformers](https://github.com/huggingface/transformers)**: For providing state-of-the-art machine learning models.
- **[Python-Levenshtein](https://github.com/ztane/python-Levenshtein)**: For fast and efficient Levenshtein distance computation.
- **[SpeechRecognition](https://github.com/Uberi/speech_recognition)**: For converting speech to text.


-----------------
### How to Use:

1. **Save the Files**: 
   - Save the Python script as `main.py`.
   - Save the batch script as `requirements.bat`.
   - Save the README content as `README.md` in your project directory.

2. **Run the Batch Script**: 
   - Double-click the `requirements.bat` file to install all necessary packages.
   - If an error occurs during installation, the script will notify you and stop.

3. **Run the Main Script**: 
   - After installing the dependencies, run `main.py` to start the application.

This setup should provide everything you need to get the project up and running, with clear instructions and a straightforward workflow.




