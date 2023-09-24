import pyaudio
import numpy as np
import subprocess
import json
from vosk import Model, KaldiRecognizer

# Set up PyAudio
p = pyaudio.PyAudio()
model = Model(model_name("vosk-model-en-us-0.22"))
rec = KaldiRecognizer(model, FRAME_RATE)

CHANNELS = 1
FRAME_RATE = 16000
RECORD_TIME = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2


# Define callback function to read audio data
def callback(in_data, frame_count, time_info, status):
    audio_data = np.frombuffer(in_data, dtype=np.int16)
    print(audio_data)  # Print audio data to terminal

    return (in_data, pyaudio.paContinue)

# Open audio stream with microphone input
stream = p.open(format=AUDIO_FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                input_device_index=2,
                frames_per_buffer=1024,
                stream_callback=callback)

# Start audio stream
stream.start_stream()

# Keep the script running to continue recording
while stream.is_active():
    pass

# Stop audio stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()