import numpy as np

with open("input.txt") as f:
    tl = f.readlines()

input = [[int(n) for n in l.split(" ")] for l in tl]

def is_safe(arr):
    if arr[0] < arr[1]:
        min = 1
        max = 3
    else:
        min = -3
        max = -1
    for i in range(1, len(arr)):
        d = arr[i] - arr[i-1]
        if d > max or d < min:
            return 0
    return 1

safe_arrs = [is_safe(x) for x in input]
print(np.sum(safe_arrs))
