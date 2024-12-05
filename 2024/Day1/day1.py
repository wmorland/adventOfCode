import numpy as np

data = np.loadtxt("input.txt", dtype=int, unpack=True)

col1 = data[0]
col2 = data[1]

sort1 = np.sort(col1)
sort2 = np.sort(col2)

s = 0
for i in range(len(sort1)):
    s += abs(sort1[i]-sort2[i])

print(s)
