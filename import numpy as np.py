import numpy as np
import simpleaudio as sa

frequency = 440  # Hz (A4 note)
duration = 2  # seconds
sample_rate = 44100  # samples per second

# Generate time points
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Generate sine wave
amplitude = 0.5  # Adjust volume
audio = amplitude * np.sin(2 * np.pi * frequency * t)

# Normalize to 16-bit integers
audio *= 32767 / np.max(np.abs(audio))
audio = audio.astype(np.int16)

# Play the audio
play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
play_obj.wait_done()