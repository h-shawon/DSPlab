import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Given specifications
M = 32  # Filter length
fp1 = 0.2  # Passband edge frequency 1 (normalized)
fp2 = 0.35  # Passband edge frequency 2 (normalized)
fs1 = 0.1  # Stopband edge frequency 1 (normalized)
fs2 = 0.425  # Stopband edge frequency 2 (normalized)

# Design the FIR bandpass filter using firwin
# firwin2 allows for the design of arbitrary FIR filters
# Use a Blackman window
h = firwin(M, [fs1, fp1, fp2, fs2], pass_zero=False, window='blackman')

# Frequency response of the filter
w, h_response = freqz(h, worN=8000)

# Plot the FIR filter coefficients
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(h, basefmt=" ")
plt.title('FIR Bandpass Filter Coefficients')
plt.xlabel('Coefficient Index')
plt.ylabel('Amplitude')
plt.grid()

# Plot the magnitude response of the filter
plt.subplot(3, 1, 2)
plt.plot(0.5 * w / np.pi, np.abs(h_response), 'b')
plt.title('Frequency Response')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude')
plt.grid()
plt.axvline(fp1, color='r', linestyle='--', label='Passband edge 1')
plt.axvline(fp2, color='g', linestyle='--', label='Passband edge 2')
plt.axvline(fs1, color='c', linestyle='--', label='Stopband edge 1')
plt.axvline(fs2, color='m', linestyle='--', label='Stopband edge 2')
plt.legend()

# Plot the magnitude response in dB
plt.subplot(3, 1, 3)
plt.plot(0.5 * w / np.pi, 20 * np.log10(np.abs(h_response)), 'b')
plt.title('Frequency Response (dB)')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(fp1, color='r', linestyle='--', label='Passband edge 1')
plt.axvline(fp2, color='g', linestyle='--', label='Passband edge 2')
plt.axvline(fs1, color='c', linestyle='--', label='Stopband edge 1')
plt.axvline(fs2, color='m', linestyle='--', label='Stopband edge 2')
plt.legend()

plt.tight_layout()
plt.show()

# Print the filter coefficients
print("Filter Coefficients:")
print(h)
