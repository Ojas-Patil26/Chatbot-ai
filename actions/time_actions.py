from datetime import datetime, date
from modules.voice_output import speak

def tell_time():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    speak(f"The time is {time_str}")

def tell_date():
    today = date.today()
    speak(f"Today is {today.strftime('%A, %B %d, %Y')}")


def greet_user():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Night Coding vibes!!!"

    