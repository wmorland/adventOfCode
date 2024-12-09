import re

total = 0

with open("input.txt") as f:
    for l in f.readlines():
        matches = re.findall(r"(?:mul\()(\d+,\d+)(?:\))", l)
        for match in matches:
            a, b = match.split(",", 1)
            total += int(a) * int(b)

print(total)
