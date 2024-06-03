import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, lfilter

# Define the parameters
fs = 100  # Sampling rate in Hz
t = np.arange(100) / fs  # Time vector (100 samples)

# Create the signal with three sinusoidal components
f1, f2, f3 = 5, 15, 30  # Frequencies in Hz
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t)

# Plot the original signal in the time domain
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, s, label='Original Signal')
plt.title('Original Signal in Time Domain')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Design notch filters to suppress 5 Hz and 30 Hz components
# Design notch filter for 5 Hz
wo1 = 5 / (fs / 2)  # Normalized frequency
Q1 = 30  # Quality factor
b1, a1 = iirnotch(wo1, Q1)

# Design notch filter for 30 Hz
wo2 = 30 / (fs / 2)  # Normalized frequency
Q2 = 30  # Quality factor
b2, a2 = iirnotch(wo2, Q2)

# Apply the filters to the signal
s_filtered = lfilter(b1, a1, s)
s_filtered = lfilter(b2, a2, s_filtered)

# Plot the filtered signal in the time domain
plt.subplot(2, 1, 2)
plt.plot(t, s_filtered, label='Filtered Signal', color='orange')
plt.title('Filtered Signal in Time Domain')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Print the filter coefficients
print("Notch filter coefficients for 5 Hz:")
print("b1 =", b1)
print("a1 =", a1)
print("\nNotch filter coefficients for 30 Hz:")
print("b2 =", b2)
print("a2 =", a2)
