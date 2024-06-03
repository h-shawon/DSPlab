import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    """
    Compute the Discrete Fourier Transform of the 1D array x
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def IDFT(X):
    """
    Compute the Inverse Discrete Fourier Transform of the 1D array X
    """
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    return x / N

# Parameters
N = 1024  # Number of samples
k = np.arange(N)  # Sample points

# Signal definition
f = 0.25 + 2 * np.sin(2 * np.pi * 5 * k / N) + np.sin(2 * np.pi * 12.5 * k / N) + 1.5 * np.sin(2 * np.pi * 20 * k / N) + 0.5 * np.sin(2 * np.pi * 35 * k / N)

# Compute the DFT
F = DFT(f)

# Compute the magnitude of the spectrum
magnitude = np.abs(F)

# Compute the IDFT
f_reconstructed = IDFT(F)

# Plot the original signal
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(k, f.real, label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Plot the magnitude spectrum
frequencies = np.fft.fftfreq(N)

plt.subplot(3, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()

# Plot the reconstructed signal
plt.subplot(3, 1, 3)
plt.plot(k, f_reconstructed.real, label='Reconstructed Signal')
plt.title('Reconstructed Signal (from IDFT)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
