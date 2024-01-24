import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not hear your request. Please repeat.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

    return query.lower()

def desktop_assistant():
    wish_me()

    while True:
        query = take_command()

        if 'open website' in query:
            speak("Sure, which website would you like to open?")
            website = take_command()
            webbrowser.open(f"https://www.{website}.com")

        elif 'open folder' in query:
            speak("Sure, please provide the folder path.")
            folder_path = take_command()
            try:
                os.startfile(r"C:\Users\pidap\OneDrive\Desktop\hi.txt")
            except Exception as e:
                speak(f"Sorry, I encountered an error: {e}")

        elif 'what is the time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break

        elif 'east or west ' in query:
            speak("charan! loves someone.")
            break

        else:
            responses = ["I'm sorry, I don't understand that command.",
                         "Could you please repeat that?",
                         "I'm still learning. Can you provide a different command?"]
            speak(random.choice(responses))

if __name__ == "__main__":
    desktop_assistant()