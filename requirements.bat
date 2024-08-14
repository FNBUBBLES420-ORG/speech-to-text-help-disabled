@echo off
echo ============================
echo Installing Python Packages...
echo ============================

:: Install torch
echo.
echo ============================
echo Installing torch...
echo ============================
pip install torch
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install torch.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo torch installed successfully.
    echo ============================
    echo.
)

:: Install transformers
echo.
echo ============================
echo Installing transformers...
echo ============================
pip install transformers
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install transformers.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo transformers installed successfully.
    echo ============================
    echo.
)

:: Install pydub
echo.
echo ============================
echo Installing pydub...
echo ============================
pip install pydub
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install pydub.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo pydub installed successfully.
    echo ============================
    echo.
)

:: Install librosa
echo.
echo ============================
echo Installing librosa...
echo ============================
pip install librosa
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install librosa.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo librosa installed successfully.
    echo ============================
    echo.
)

:: Install fuzzywuzzy
echo.
echo ============================
echo Installing fuzzywuzzy...
echo ============================
pip install fuzzywuzzy
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install fuzzywuzzy.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo fuzzywuzzy installed successfully.
    echo ============================
    echo.
)

:: Install nltk
echo.
echo ============================
echo Installing nltk...
echo ============================
pip install nltk
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install nltk.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo nltk installed successfully.
    echo ============================
    echo.
)

:: Install soundfile
echo.
echo ============================
echo Installing soundfile...
echo ============================
pip install soundfile
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install soundfile.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo soundfile installed successfully.
    echo ============================
    echo.
)

:: Install tk
echo.
echo ============================
echo Installing tk...
echo ============================
pip install tk
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install tk.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo tk installed successfully.
    echo ============================
    echo.
)

:: Install python-Levenshtein
echo.
echo ============================
echo Installing python-Levenshtein...
echo ============================
pip install python-Levenshtein
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install python-Levenshtein.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo python-Levenshtein installed successfully.
    echo ============================
    echo.
)

:: Install SpeechRecognition
echo.
echo ============================
echo Installing SpeechRecognition...
echo ============================
pip install SpeechRecognition
if errorlevel 1 (
    echo.
    echo ============================
    echo ERROR: Failed to install SpeechRecognition.
    echo Please check your internet connection or the package name.
    echo ============================
    pause
    exit /b 1
) else (
    echo.
    echo ============================
    echo SpeechRecognition installed successfully.
    echo ============================
    echo.
)

echo.
echo ============================
echo All packages installed successfully.
echo ============================
pause
