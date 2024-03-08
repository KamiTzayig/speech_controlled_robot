import requests
import time
from pvrecorder import PvRecorder
from wakeup_word_test import detect_wake_up_word

SERVER_URL = "http://localhost:8888/"

is_awake = False

def send(path):
    try:
        response = requests.get(SERVER_URL + path)
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(e)


recorder = PvRecorder(frame_length=512,)
recorder.start()

while True:
    audio_frame = recorder.read()
    wakeup = detect_wake_up_word(audio_frame=audio_frame)
    if wakeup == "hajimete":
        is_awake = True
        send("wakeup/start")
    elif wakeup == "tomare":
        is_awake = False
        send("wakeup/stop")

    if is_awake:
        pass

  