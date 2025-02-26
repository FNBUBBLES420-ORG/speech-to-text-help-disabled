# Speech to Text Application 🎙️✨

🎙️ Welcome to the Speech to Text Application! 📝 This tool converts your spoken words into text in real time. With a sleek, modern interface powered by `customtkinter`, you can easily integrate this solution into your streaming setup or any project that needs speech-to-text capabilities. 🌟

## Features 🚀
- **Real-time Speech Recognition**: Convert your speech to text on the fly using Google Speech Recognition.
- **User-friendly GUI**: Enjoy a modern and intuitive interface built with `customtkinter`.
- **Configurable Settings**: Easily adjust ambient noise calibration, timeout durations, and more via `config.py`.
- **Live Transcription**: See the transcribed text update live on-screen and save it to a file (`transcription.txt`) for further use.
- **OBS Integration**: Seamlessly use the saved transcription file for live captioning in OBS.

## Installation 🛠️

## 📥 How to Download the Repo (First-Time Users)

--> Click the link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos) 📄.

1. Install Python
- use the `python3119.bat` to install python 3119. just double click on the batch file and if a blue window pops up, click more and next,
- follow the directions on the terminal in the `cmd.exe`
- script will do it all for you.
- after open up `cmd.exe` a new one and type
  ```
  python --version
  ```
  - `output` will be Python 3.11.9

3. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

4. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure the Application**:
    - Open the `config.py` file to adjust settings like ambient noise duration, timeout, and phrase time limits.

## Usage 🎤

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **How to Use**:
    - Click the **"Start Listening"** button to begin capturing your speech.
    - Speak clearly into your microphone—the transcribed text will appear in the text area.
    - The transcription is also saved in `transcription.txt` for use with OBS or any other application.
    - Click **"Close"** to exit the application.

## Using with OBS 📺

To integrate the transcription with OBS for live captioning, follow these steps:

1. **Open OBS**.
2. **Add a Text Source**:
   - Click the **"+"** button in the **Sources** panel.
   - Select **"Text (GDI+)"** on Windows or **"Text (FreeType 2)"** on other systems.
   - Name your text source (e.g., "Live Captions").
3. **Enable File Reading**:
   - Check the **"Read from file"** option.
   - Click **"Browse"** and select the `transcription.txt` file from your project directory.
4. **Customize Appearance**:
   - Adjust the font, color, size, and alignment to match your stream's style.
5. **Position Your Captions**:
   - Drag and drop the text source to your desired location on the OBS canvas.
6. **Start Your Stream**:
   - As the application writes new transcriptions to the file, OBS will automatically update the captions in real time!

## Configuration ⚙️

The `config.py` file includes the following settings:

- **APPEARANCE_MODE**: Set to `"dark"` or `"light"` for the GUI.
- **THEME_COLOR**: Choose your desired theme color (e.g., `"blue"`).
- **FONT**: Define the font type and size (e.g., `('Helvetica', 10)`).
- **AMBIENT_NOISE_ADJUSTMENT_DURATION**: Duration in seconds for ambient noise calibration.
- **TIMEOUT_DURATION**: Maximum time (in seconds) to wait for speech to start.
- **PHRASE_TIME_LIMIT**: Maximum duration (in seconds) to capture a single phrase.

## Troubleshooting ❓

- **Speech Not Detected**: Ensure your microphone is working correctly and consider increasing the ambient noise adjustment duration in `config.py`.
- **Incorrect Transcription**: Speak clearly and check your internet connection since the application relies on Google's online speech recognition service.

## Need Help??
- Join the Discord [https://discord.fnbubbles420.org/invite](https://discord.fnbubbles420.org/invite)

## Contributing 🤝

Contributions are welcome! Please open issues or submit pull requests if you'd like to help improve this project.

## License 📄

[Private License](https://github.com/FNBUBBLES420-ORG/speech-to-text-help-disabled/blob/main/LICENSE.md)

---

Enjoy converting your voice to text with this awesome application! If you have any questions or feedback, feel free to reach out. Happy coding! 😃
