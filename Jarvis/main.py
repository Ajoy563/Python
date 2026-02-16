# SpeechRecognition – A Python module used to convert spoken audio into text using speech-to-text engines.
# PyAudio – A Python module that allows recording and playing audio through the system microphone and speakers.
# setuptools – A Python utility module used for packaging, installing, and distributing Python projects.
# pyttsx3 – A Python text-to-speech module that converts text into spoken voice offline.
# webbrowser – A built-in Python module used to open URLs in the system’s default web browser.

import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
import pygame
import subprocess
import os
from gtts import gTTS
import sys


HF_API_KEY = os.getenv("HF_API_KEY")
HF_API_URL = "https://router.huggingface.co/v1/chat/completions"
HF_HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}
# print("HF_API_KEY:", HF_API_KEY)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def exitJarvis():
    speak("Goodbye sir. Shutting down.")
    sys.exit(0)
    
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 



import time

def aiProcess(command):
    payload = {
        "model": "google/flan-t5-base",
        "messages": [
            {"role": "system", "content": "Answer clearly and simply."},
            {"role": "user", "content": command}
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(
            HF_API_URL,
            headers=HF_HEADERS,
            json=payload,
            timeout=60
        )

        data = response.json()

        if "error" in data:
            return data["error"].get("message", "AI error occurred.")

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("AI error:", e)
        return "AI service is currently unavailable."
    
    
def processCommand(c):
    if "jarvis exit" in c or c in ["exit","stop"]:
        exitJarvis()
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=30d0572b0f0e4fa59ceb28820319324b")
        if r.status_code == 200:
            # Parse the JSON response
            data  = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Speak the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
        
if __name__ == "__main__":
    print(aiProcess("What is force?"))
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            word = word.lower()

            if(word == "jarvis"):
                speak("Yes sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command: ", command)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
