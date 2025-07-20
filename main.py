from modules.voice_input import listen_to_user
from modules.voice_output import speak
from actions.time_actions import tell_time, tell_date


def main():
    name = input("Please enter your name: ")
    speak(f"Hello {name}, how can I assist you today?")

    while True:
        user_input = listen_to_user()

        if not user_input:
            continue

        if "exit" in user_input.lower() or "quit" in user_input.lower() or "goodbye" in user_input.lower():
            speak(f"Goodbye {name}! Hope you have a great day.")
            break

        elif "time" in user_input.lower():
            tell_time()

        elif "date" in user_input.lower():
            tell_date()

        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()

