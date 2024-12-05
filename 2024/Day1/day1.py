import numpy as np

# Load the data and sort the columns directly
col1, col2 = np.loadtxt("input.txt", dtype=int, unpack=True)

# Sort both columns and compute the sum of absolute differences
s = np.sum(np.abs(np.sort(col1) - np.sort(col2)))

print(s)

# Part 2
values, counts = np.unique(col2, return_counts=True)

freq = dict(zip(values, counts))

similarity = 0
for i in range(len(col1)):
    if (col1[i] in freq):
        similarity += col1[i] * freq[col1[i]]

print(similarity)
