import numpy as np
import matplotlib.pyplot as plt

# 1. Sampling
def sample_signal(signal, sample_rate):
    """
    Sample the continuous signal at the given sample rate.
    """
    t = np.arange(0, len(signal), sample_rate)
    sampled_signal = signal[t]
    return t, sampled_signal

# 2. Quantization
def quantize_signal(signal, num_levels):
    """
    Quantize the sampled signal to the specified number of levels.
    """
    min_val = np.min(signal)
    max_val = np.max(signal)
    quantization_levels = np.linspace(min_val, max_val, num_levels)
    quantized_signal = np.digitize(signal, quantization_levels) - 1
    quantized_signal = quantization_levels[quantized_signal]
    return quantized_signal

# 3. Coding
def encode_signal(signal, num_levels):
    """
    Encode the quantized signal into binary code.
    """
    num_bits = int(np.ceil(np.log2(num_levels)))
    encoded_signal = [format(int(x), f'0{num_bits}b') for x in signal]
    return encoded_signal

# Generate a continuous signal (sine wave)
fs = 1000  # Original sampling frequency
t_continuous = np.linspace(0, 1, fs)
continuous_signal = 2 * np.sin(2 * np.pi * 5 * t_continuous) + 1.5 * np.sin(2 * np.pi * 20 * t_continuous)

# Perform sampling
sample_rate = 10  # Downsampling factor
t_sampled, sampled_signal = sample_signal(continuous_signal, sample_rate)

# Perform quantization
num_levels = 16  # Number of quantization levels
quantized_signal = quantize_signal(sampled_signal, num_levels)

# Perform coding
encoded_signal = encode_signal(quantized_signal, num_levels)

# Plot the signals
plt.figure(figsize=(12, 8))

# Plot the continuous signal
plt.subplot(3, 1, 1)
plt.plot(t_continuous, continuous_signal, label='Continuous Signal')
plt.title('Continuous Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

# Plot the sampled signal
plt.subplot(3, 1, 2)
plt.stem(t_sampled, sampled_signal, basefmt=" ", label='Sampled Signal')
plt.title('Sampled Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid()

# Plot the quantized signal
plt.subplot(3, 1, 3)
plt.stem(t_sampled, quantized_signal, basefmt=" ", label='Quantized Signal')
plt.title('Quantized Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()

# Print the encoded signal
print("Encoded Signal:")
for i, code in enumerate(encoded_signal):
    print(f"Sample {i}: {code}")
