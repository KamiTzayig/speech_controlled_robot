from pvrecorder import PvRecorder
import pvrhino
from api_keys import ACCESS_KEY
CONTEXT_FILE_PATH = r"test_en_windows_v3_0_0.rhn"


rhino = pvrhino.create(
   access_key= ACCESS_KEY,
   context_path=CONTEXT_FILE_PATH
)


recorder = PvRecorder(
    frame_length=rhino.frame_length,)
recorder.start()

while True:
    audio_frame = recorder.read()
    is_finalized = rhino.process(audio_frame)
    if is_finalized:
        # get inference if is_finalized is true
        inference = rhino.get_inference()
        if inference.is_understood:
            # use intent and slots if inference was understood
            intent = inference.intent
            slots = inference.slots
            print(intent)
            print(slots)

