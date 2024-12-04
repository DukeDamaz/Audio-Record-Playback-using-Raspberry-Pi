import os
import wave
import pyaudio
from pydub import AudioSegment
import time
import pygame
import RPi.GPIO as GPIO

# GPIO pin setup for push buttons
RECORD_PIN = 17  # Change as per your connection
PLAY_PIN = 27    # Change as per your connection

# File and directory setup
SAVE_DIR = "/home/pi/recordings"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RECORD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PLAY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize Pygame for audio playback
pygame.mixer.init()

# Initialize PyAudio for recording
p = pyaudio.PyAudio()

# Function to record audio
def record_audio(filename):
    print("Recording started...")
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
    
    frames = []
    while True:
        if GPIO.input(RECORD_PIN) == GPIO.LOW:  # Button pressed
            print("Recording...")
            data = stream.read(1024)
            frames.append(data)
        elif GPIO.input(RECORD_PIN) == GPIO.HIGH and frames:
            print("Recording stopped...")
            break
        time.sleep(0.1)
    
    stream.stop_stream()
    stream.close()

    # Save as .wav file first
    wav_filename = os.path.join(SAVE_DIR, filename + ".wav")
    with wave.open(wav_filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))

    # Convert the .wav file to .mp3 using pydub
    mp3_filename = os.path.join(SAVE_DIR, filename + ".mp3")
    sound = AudioSegment.from_wav(wav_filename)
    sound.export(mp3_filename, format="mp3")

    # Optionally delete the .wav file after conversion
    os.remove(wav_filename)
    print(f"Audio saved as {mp3_filename}")

# Function to play audio
def play_audio(filename):
    mp3_filename = os.path.join(SAVE_DIR, filename + ".mp3")
    if os.path.exists(mp3_filename):
        print(f"Playing {mp3_filename}...")
        pygame.mixer.music.load(mp3_filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until playback finishes
            time.sleep(0.1)
    else:
        print("No audio file found to play.")

# Main loop
try:
    while True:
        if GPIO.input(PLAY_PIN) == GPIO.LOW:  # Play button pressed
            play_audio("recorded_audio")  # You can change filename accordingly
            time.sleep(1)  # Debounce time
        elif GPIO.input(RECORD_PIN) == GPIO.LOW:  # Record button pressed
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            record_audio(timestamp)  # Record audio and save with timestamp
            time.sleep(1)  # Debounce time
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated.")
finally:
    GPIO.cleanup()
    p.terminate()
