import pyaudio
import numpy as np
import noisereduce as nr
import wave
import requests

# Set parameters for PyAudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
headers = {"Authorization": "Bearer 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"}

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening...")

while True:
    # Record audio input
    frames = []
    for i in range(0, int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Convert audio input to numpy array
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE)

    # Save cleaned audio to WAV file
    # with wave.open("cleaned_audio.wav", "wb") as wav_file:
    #     wav_file.setnchannels(CHANNELS)
    #     wav_file.setsampwidth(p.get_sample_size(FORMAT))
    #     wav_file.setframerate(RATE)
    #     wav_file.writeframes(reduced_noise.tobytes())

    # response = requests.post(API_URL, headers=headers, data=reduced_noise.all())
    # print(response.json())