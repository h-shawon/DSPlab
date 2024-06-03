import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Given specifications
fp = 1500  # Passband edge in Hz
transition_width = 500  # Transition width in Hz
fs = 10000  # Sampling frequency in Hz
N = 67  # Filter length

# Calculate the cutoff frequency
fc = fp + transition_width / 2  # Center of the transition band

# Normalized frequencies
wc = fc / (fs / 2)  # Cutoff frequency normalized by Nyquist frequency

# Design the FIR filter using firwin with Blackman window
h = firwin(N, wc, window='blackman')

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
plt.plot(0.5 * fs * w / np.pi, np.abs(h_response), 'b')
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.axvline(fp, color='r', linestyle='--', label='Passband edge')
plt.axvline(fc, color='g', linestyle='--', label='Cutoff frequency')
plt.legend()

# Plot the magnitude response in dB
plt.subplot(3, 1, 3)
plt.plot(0.5 * fs * w / np.pi, 20 * np.log10(np.abs(h_response)), 'b')
plt.title('Frequency Response (dB)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(fp, color='r', linestyle='--', label='Passband edge')
plt.axvline(fc, color='g', linestyle='--', label='Cutoff frequency')
plt.legend()

plt.tight_layout()
plt.show()

# Print the filter coefficients
print("Filter Coefficients:")
print(h)
