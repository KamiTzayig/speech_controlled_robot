import pvporcupine
from pvrecorder import PvRecorder
from api_keys import ACCESS_KEY
KEYWORD_FILE_PATH_1 = r"C:\Users\dyeko\Documents\python\wakeup-word\始めて_ja_windows_v3_0_0.ppn"
KEYWORD_FILE_PATH_2 = r"C:\Users\dyeko\Documents\python\wakeup-word\止まれ_ja_windows_v3_0_0.ppn"
MODEL_FILE_PATH = r"C:\Users\dyeko\Documents\python\wakeup-word\porcupine_params_ja.pv"

porcupine = pvporcupine.create(
access_key= ACCESS_KEY,
keywords=['picovoice', 'bumblebee'],
keyword_paths=[KEYWORD_FILE_PATH_1, KEYWORD_FILE_PATH_2],
model_path=MODEL_FILE_PATH)

recorder = PvRecorder(
    frame_length=porcupine.frame_length,)
recorder.start()




while True:
  audio_frame = recorder.read()
  keyword_index = porcupine.process(audio_frame)
  if keyword_index == 0:
      print('detected hajimete')
  elif keyword_index == 1:
      print('tomare detected')

  



porcupine.delete()