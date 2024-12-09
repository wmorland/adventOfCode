import re


def calc_mul_for_string(total, l):
    matches = re.findall(r"(?:mul\()(\d+,\d+)(?:\))", l)
    for match in matches:
        a, b = match.split(",", 1)
        total += int(a) * int(b)
    return total


with open("input.txt") as f:
    l = f.read()

total = 0
total = calc_mul_for_string(total, l)
print(total)

total = 0
enablers = l.split("do()")
for enabled in enablers:
    calc = enabled.split("don't()", 1)[0]
    total = calc_mul_for_string(total, calc)
print(total)
