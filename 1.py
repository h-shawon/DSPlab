import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1024  # Number of samples
k = np.arange(N)  # Sample points

# Signal definition
f = 0.25 + 2 * np.sin(2 * np.pi * 5 * k / N) + np.sin(2 * np.pi * 12.5 * k / N) + 1.5 * np.sin(2 * np.pi * 20 * k / N) + 0.5 * np.sin(2 * np.pi * 35 * k / N)

# Compute the DFT
F = np.fft.fft(f)
# Get the magnitude of the spectrum
magnitude = np.abs(F)
# Frequency axis
frequencies = np.fft.fftfreq(N)

# Plot the magnitude spectrum
plt.figure(figsize=(10, 6))
plt.plot(frequencies, magnitude)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.show()
