import numpy as np
import matplotlib.pyplot as plt

# Define two sequences
sequence1 = np.array([1, 2, 3, 4, 5])
sequence2 = np.array([5, 6, 7, 8, 9])

# Convolution
def convolve_sequences(seq1, seq2):
    return np.convolve(seq1, seq2)

# Correlation
def correlate_sequences(seq1, seq2):
    return np.correlate(seq1, seq2, mode='full')

# Perform convolution
convolution_result = convolve_sequences(sequence1, sequence2)

# Perform correlation
correlation_result = correlate_sequences(sequence1, sequence2)

# Print the results
print("Sequence1: ", sequence1)
print("Sequence2: ", sequence2)
print("Convolution Result:", convolution_result)
print("Correlation Result:", correlation_result)

# Plot the sequences
plt.figure(figsize=(12, 10))

# Plot the first sequence
plt.subplot(4, 1, 1)
plt.stem(sequence1, basefmt=" ")
plt.title('Sequence 1')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.grid()

# Plot the second sequence
plt.subplot(4, 1, 2)
plt.stem(sequence2, basefmt=" ")
plt.title('Sequence 2')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.grid()

# Plot the convolution result
plt.subplot(4, 1, 3)
plt.stem(convolution_result, basefmt=" ")
plt.title('Convolution of Sequence 1 and Sequence 2')
plt.xlabel('Index')
plt.ylabel('Amplitude')
plt.grid()

# Plot the correlation result
plt.subplot(4, 1, 4)
plt.stem(correlation_result, basefmt=" ")
plt.title('Correlation of Sequence 1 and Sequence 2')
plt.xlabel('Lag')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()


