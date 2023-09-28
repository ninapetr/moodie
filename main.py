import pyaudio
import numpy as np
import subprocess
import json
from vosk import Model, KaldiRecognizer

FRAME_RATE = 16000
CHANNELS = 1
FRAMES_PER_BUFFER = 8192
AUDIO_FORMAT = pyaudio.paInt16


mic = pyaudio.PyAudio()
model = Model(model_name="vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, FRAME_RATE)

stream = mic.open(channels = CHANNELS,
                format = AUDIO_FORMAT,
                rate = FRAME_RATE,
                input = True,
                frames_per_buffer=FRAMES_PER_BUFFER)

stream.start_stream()

while True:
    data = stream.read(4096)
    if rec.AcceptWaveform(data):
        result = rec.Result()
        text = json.loads(result)["text"]
