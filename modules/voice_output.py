import pyttsx3

def get_ava_enhanced_voice(engine):
    for voice in engine.getProperty('voices'):
        if voice.id == 'com.apple.voice.enhanced.en-US.Ava':
            return voice
    return None

def speak(text):
    engine = pyttsx3.init()
    voice = get_ava_enhanced_voice(engine)
    
    if voice:
        engine.setProperty('voice', voice.id)
    else:
        print("Ava (Enhanced) voice not found. Using default voice.")

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I'm using the Ava Enhanced voice for speech synthesis.")
