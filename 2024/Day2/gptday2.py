# Read and parse the input
with open("input.txt") as f:
    input_data = [list(map(int, line.split())) for line in f]


def is_safe(arr, use_damper=False):
    """Checks if an array is safe based on its consecutive differences."""
    min_diff, max_diff = (1, 3) if arr[0] < arr[1] else (-3, -1)
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if not (min_diff <= diff <= max_diff):
            if use_damper:
                # Try removing one element and re-checking
                for j in range(len(arr)):
                    if is_safe(arr[:j] + arr[j + 1 :]):
                        return 1
            return 0
    return 1


# Check arrays for safety
safe_count = sum(is_safe(arr) for arr in input_data)
damper_safe_count = sum(is_safe(arr, use_damper=True) for arr in input_data)

print(safe_count)
print(damper_safe_count)
