import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Given specifications
fp = 2000  # Passband edge in Hz
fs = 5000  # Stopband edge in Hz
f_sampling = 20000  # Sampling frequency in Hz
N = 21  # Filter length

# Normalized frequencies
wp = fp / (f_sampling / 2)
ws = fs / (f_sampling / 2)

# Design the FIR filter using firwin with Hanning window
h = firwin(N, [wp, ws], pass_zero=False, window='hann')

# Frequency response of the filter
w, h_response = freqz(h, worN=8000)

# Plot the FIR filter coefficients
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(h, basefmt=" ")
plt.title('FIR Filter Coefficients')
plt.xlabel('Coefficient Index')
plt.ylabel('Amplitude')
plt.grid()

# Plot the magnitude response of the filter
plt.subplot(3, 1, 2)
plt.plot(0.5 * f_sampling * w / np.pi, np.abs(h_response), 'b')
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.axvline(fp, color='r', linestyle='--', label='Passband edge')
plt.axvline(fs, color='g', linestyle='--', label='Stopband edge')
plt.legend()

# Plot the magnitude response in dB
plt.subplot(3, 1, 3)
plt.plot(0.5 * f_sampling * w / np.pi, 20 * np.log10(np.abs(h_response)), 'b')
plt.title('Frequency Response (dB)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(fp, color='r', linestyle='--', label='Passband edge')
plt.axvline(fs, color='g', linestyle='--', label='Stopband edge')
plt.legend()

plt.tight_layout()
plt.show()

# Print the filter coefficients
print("Filter Coefficients:", h)
