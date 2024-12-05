import numpy as np

# Load the data and sort the columns directly
col1, col2 = np.loadtxt("input.txt", dtype=int, unpack=True)

# Sort both columns and compute the sum of absolute differences
s = np.sum(np.abs(np.sort(col1) - np.sort(col2)))

print(s)
