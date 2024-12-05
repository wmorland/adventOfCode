import numpy as np

# Load the data and sort the columns directly
col1, col2 = np.loadtxt("input.txt", dtype=int, unpack=True)

# Sort both columns and compute the sum of absolute differences
s = np.sum(np.abs(np.sort(col1) - np.sort(col2)))

print(s)

# Part 2: Calculate similarity score based on frequency in the second array
values, counts = np.unique(col2, return_counts=True)
freq = dict(zip(values, counts))

# Compute similarity score using a list comprehension
similarity = sum(val * freq[val] for val in col1 if val in freq)
print(similarity)
