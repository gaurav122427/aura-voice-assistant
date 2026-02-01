import speech_recognition as sr
import pyttsx3
from duckduckgo_search import DDGS
import requests
conversation_memory = []

# ------------------ SPEECH SETUP ------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

# ------------------ AI (OLLAMA) ------------------
def ask_ai(prompt):
    # store user message
    conversation_memory.append(f"User: {prompt}")

    # build prompt with memory
    full_prompt = "\n".join(conversation_memory) + "\nAura:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": full_prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    # store assistant reply
    conversation_memory.append(f"Aura: {answer}")

    # keep memory short (important)
    if len(conversation_memory) > 10:
        conversation_memory.pop(0)

    return answer

# ------------------ TOOL ------------------
def search_tool(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
        return results[0]["body"] if results else "No results found."

# ------------------ AGENT LOGIC ------------------
def agent(query):
    query = query.lower()

    if "time" in query:
        from datetime import datetime
        return datetime.now().strftime("The time is %H:%M")

    elif "search" in query or "internet" in query:
        return search_tool(query)

    else:
        return ask_ai(query)

# ------------------ MAIN LOOP ------------------
speak("Hello, I am Aura. Ask me anything.")

while True:
    query = listen()

    if "exit" in query.lower():
        speak("Goodbye")
        break

    if query:
        response = agent(query)
        print("Aura:", response)
        speak(response)