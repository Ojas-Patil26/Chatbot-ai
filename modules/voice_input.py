import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."
    except sr.RequestError as e:
        return f"Could not request results; {e}"
