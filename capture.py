import pyautogui
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time
import threading
import os

# Create a directory to store captured data
if not os.path.exists("captures"):
    os.makedirs("captures")

def capture_screen_audio():
    while True:
        timestamp = int(time.time())
        
        # Capture screen
        screenshot = pyautogui.screenshot()
        screenshot.save(f'captures/screenshot_{timestamp}.png')
        
        # Capture audio
        duration = 1  # seconds
        fs = 44100  # Sample rate
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype=np.int16)
        sd.wait()
        write(f'captures/audio_{timestamp}.wav', fs, recording)
        
        # Capture mouse position
        mouse_pos = pyautogui.position()
        with open(f'captures/mouse_{timestamp}.txt', 'w') as f:
            f.write(f'Mouse position: {mouse_pos}\n')
        
        time.sleep(1)

def start_capture():
    capture_thread = threading.Thread(target=capture_screen_audio)
    capture_thread.daemon = True
    capture_thread.start()

if __name__ == "__main__":
    start_capture()
    input("Press Enter to stop...\n")
