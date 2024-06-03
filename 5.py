import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy.signal as signal

# Load speech signal from a WAV file
fs, speech_signal = wavfile.read('sample2.wav')

# Normalize the signal
speech_signal = speech_signal / np.max(np.abs(speech_signal))

# Parameters for frame segmentation
frame_size = int(0.02 * fs)  # 20 ms frame size
frame_shift = int(0.01 * fs)  # 10 ms frame shift

# Function to compute short-time energy
def short_time_energy(signal, frame_size, frame_shift):
    num_frames = int((len(signal) - frame_size) / frame_shift) + 1
    energy = np.zeros(num_frames)
    for i in range(num_frames):
        start = i * frame_shift
        end = start + frame_size
        frame = signal[start:end]
        energy[i] = np.sum(frame ** 2)
    return energy

# Function to compute zero-crossing rate
def zero_crossing_rate(signal, frame_size, frame_shift):
    num_frames = int((len(signal) - frame_size) / frame_shift) + 1
    zcr = np.zeros(num_frames)
    for i in range(num_frames):
        start = i * frame_shift
        end = start + frame_size
        frame = signal[start:end]
        zcr[i] = np.sum(np.abs(np.diff(np.sign(frame)))) / (2 * frame_size)
    return zcr

# Compute short-time energy and zero-crossing rate
energy = short_time_energy(speech_signal, frame_size, frame_shift)
zcr = zero_crossing_rate(speech_signal, frame_size, frame_shift)

# Thresholds for classification (adjust based on your signal)
energy_threshold = 0.02
zcr_threshold = 0.1

# Classify each frame
regions = []
for i in range(len(energy)):
    if energy[i] < energy_threshold:
        regions.append('silence')
    elif zcr[i] > zcr_threshold:
        regions.append('unvoiced')
    else:
        regions.append('voiced')

# Plot the results
time = np.arange(len(speech_signal)) / fs
frame_times = np.arange(len(energy)) * frame_shift / fs

plt.figure(figsize=(15, 8))

# Plot the speech signal
plt.subplot(3, 1, 1)
plt.plot(time, speech_signal)
plt.title('Speech Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()

# Plot the short-time energy
plt.subplot(3, 1, 2)
plt.plot(frame_times, energy)
plt.axhline(y=energy_threshold, color='r', linestyle='--', label='Energy Threshold')
plt.title('Short-Time Energy')
plt.xlabel('Time [s]')
plt.ylabel('Energy')
plt.legend()
plt.grid()

# Plot the zero-crossing rate
plt.subplot(3, 1, 3)
plt.plot(frame_times, zcr)
plt.axhline(y=zcr_threshold, color='r', linestyle='--', label='ZCR Threshold')
plt.title('Zero-Crossing Rate')
plt.xlabel('Time [s]')
plt.ylabel('ZCR')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Display regions
print("Regions:")
for i, region in enumerate(regions):
    print(f"Frame {i}: {region}")
