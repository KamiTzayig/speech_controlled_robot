import pvcheetah
from pvrecorder import PvRecorder
from api_keys import ACCESS_KEY

cheetah = pvcheetah.create(
       access_key= ACCESS_KEY,

    )

recorder = PvRecorder(
    frame_length=cheetah.frame_length,)
recorder.start()



while True:
    audio_frame = recorder.read()
    partial_transcript, is_endpoint = cheetah.process(audio_frame)
    print(partial_transcript, end='', flush=True)
    if is_endpoint:
        print(cheetah.flush())

