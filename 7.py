import numpy as np
import matplotlib.pyplot as plt

# Define the original sequence x(n)
x = np.array([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])

# Define the range of n for the original sequence
n = np.arange(len(x))
# Define the range of n for the result sequence y(n)
# We need to accommodate the shifts n-5 and n+4
n_min = n[0] - 5  # Minimum index after shift
n_max = n[-1] + 4  # Maximum index after shift
n_y = np.arange(n_min, n_max + 1)

# Create x(n-5) and x(n+4) with zero-padding where necessary
x_n_minus_5 = np.zeros_like(n_y, dtype=float)
x_n_plus_4 = np.zeros_like(n_y, dtype=float)

for i in range(len(n)):
    if n[i] - 5 in n_y:
        x_n_minus_5[n_y == n[i] - 5] = x[i]
    if n[i] + 4 in n_y:
        x_n_plus_4[n_y == n[i] + 4] = x[i]

# Compute y(n) = 2x(n - 5) - 3x(n + 4)
y = 2 * x_n_minus_5 - 3 * x_n_plus_4

# Plot the original sequence x(n)
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt=" ")
plt.title('Original Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

# Plot the shifted and scaled sequences
plt.subplot(3, 1, 2)
plt.stem(n_y, 2 * x_n_minus_5, basefmt=" ", label='2x(n-5)')
plt.stem(n_y, -3 * x_n_plus_4, basefmt=" ", label='-3x(n+4)')
plt.title('Shifted and Scaled Sequences')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Plot the resulting sequence y(n)
plt.subplot(3, 1, 3)
plt.stem(n_y, y, basefmt=" ")
plt.title('Resulting Sequence y(n) = 2x(n - 5) - 3x(n + 4)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid()

plt.tight_layout()
plt.show()

# Print the resulting sequence
print("y(n) =", y)
