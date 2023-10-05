import pyaudio
import requests

API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
headers = {"Authorization": "Bearer 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"}

FRAME_RATE = 16000
CHANNELS = 1
FRAMES_PER_BUFFER = 8192
AUDIO_FORMAT = pyaudio.paInt16

mic = pyaudio.PyAudio()
stream = mic.open(channels=CHANNELS,
                  format=AUDIO_FORMAT,
                  rate=FRAME_RATE,
                  input=True,
                  frames_per_buffer=FRAMES_PER_BUFFER)

stream.start_stream()
print("Listening...")

while True:
    data = stream.read(10096)

    # pain

    response = requests.post(API_URL, headers=headers, files={"file": ("audio.wav", wav_file)})
    print(response.json())