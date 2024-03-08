import pvporcupine
from pvrecorder import PvRecorder
from api_keys import ACCESS_KEY
KEYWORD_FILE_PATH_1 = r"始めて_ja_windows_v3_0_0.ppn"
KEYWORD_FILE_PATH_2 = r"止まれ_ja_windows_v3_0_0.ppn"
MODEL_FILE_PATH = r"porcupine_params_ja.pv"

porcupine = pvporcupine.create(
access_key= ACCESS_KEY,
keyword_paths=[KEYWORD_FILE_PATH_1, KEYWORD_FILE_PATH_2],
model_path=MODEL_FILE_PATH)

# recorder = PvRecorder(
#     frame_length=porcupine.frame_length,)
# recorder.start()


def detect_wake_up_word(audio_frame):
    keyword_index = porcupine.process(audio_frame)
    if keyword_index == 0:
      return "hajimete"
    elif keyword_index == 1:
      return "tomare"
  
    elif keyword_index != -1:
      print('detected unknown keyword')


# while True:
#     audio_frame = recorder.read()
#     result = detect_wake_up_word(audio_frame=audio_frame)
#     if result != False:
#         print(result)



# porcupine.delete()