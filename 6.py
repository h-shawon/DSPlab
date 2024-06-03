import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load speech signal from a WAV file
fs, speech_signal = wavfile.read('sample2.wav')

# Normalize the signal
speech_signal = speech_signal / np.max(np.abs(speech_signal))

# Parameters for frame segmentation
frame_size = int(0.02 * fs)  # 20 ms frame size
frame_shift = int(0.01 * fs)  # 10 ms frame shift

# Function to compute short-term auto-correlation
def short_term_autocorrelation(signal, frame_size, frame_shift):
    num_frames = int((len(signal) - frame_size) / frame_shift) + 1
    autocorrelation = []
    for i in range(num_frames):
        start = i * frame_shift
        end = start + frame_size
        frame = signal[start:end]
        # Compute auto-correlation for the frame
        autocorr = np.correlate(frame, frame, mode='full')
        autocorr = autocorr[autocorr.size // 2:]  # Take the second half
        autocorrelation.append(autocorr)
    return np.array(autocorrelation)

# Compute short-term auto-correlation
autocorrelation = short_term_autocorrelation(speech_signal, frame_size, frame_shift)

# Plot the speech signal
time = np.arange(len(speech_signal)) / fs
plt.figure(figsize=(12, 10))

plt.subplot(2, 1, 1)
plt.plot(time, speech_signal)
plt.title('Speech Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()

# Plot auto-correlation for the first few frames
num_frames_to_plot = 1
frame_times = (np.arange(num_frames_to_plot) * frame_shift) / fs

for i in range(num_frames_to_plot):
    plt.subplot(num_frames_to_plot + 1, 1, i + 2)
    plt.plot(autocorrelation[i])
    plt.title(f'Auto-correlation of Frame {i}')
    plt.xlabel('Lag')
    plt.ylabel('Amplitude')
    plt.grid()

plt.tight_layout()
plt.show()
