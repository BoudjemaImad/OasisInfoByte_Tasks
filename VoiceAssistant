import win32com.client
import datetime
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import pywhatkit

speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()

for i in range(voices.Count):
    if "english" in voices.Item(i).GetDescription().lower():
        speaker.Voice = voices.Item(i)
        break

def talk(text):
    speaker.Speak(text)

def listen(duration=3, fs=44100):
    recognizer = sr.Recognizer()
    print("Listening...")

    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    audio = sr.AudioData(audio_data.tobytes(), fs, 2)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Didn't catch that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return ""

def run_assistant():
    """Main loop for the voice assistant"""
    talk("Hello! How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            talk("Hello there!")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            talk("The time is " + now)

        elif "date" in command:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            talk("Today's date is " + today)

        elif "search" in command:
            search_query = command.replace("search", "").strip()
            if search_query:
                talk("Searching for " + search_query)
                pywhatkit.search(search_query)
            else:
                talk("Please tell me what to search for.")

        elif "stop" in command or "exit" in command:
            talk("Goodbye!")
            break

if __name__ == "__main__":
    run_assistant()
