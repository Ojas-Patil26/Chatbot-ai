import datetime
from modules.voice_output import speak

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")