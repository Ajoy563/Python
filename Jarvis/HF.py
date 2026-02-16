import os
import requests
import subprocess

HF_API_KEY = os.getenv("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")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def ask_jarvis(question):
    payload = {
        "inputs": question
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    if isinstance(data, dict) and "error" in data:
        return "Sorry sir, the service is busy right now."

    return data[0]["generated_text"]

def speak(text):
    subprocess.run(["say", "-v", "Alex", text])

print("Jarvis is online. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        speak("Goodbye sir.")
        break

    answer = ask_jarvis(user_input)
    print("Jarvis:", answer)
    speak(answer)