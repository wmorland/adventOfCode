import re


def calc_mul_for_string(total, text):
    """
    Calculates the sum of products for all 'mul(a,b)' patterns in the given text.
    """
    matches = re.findall(r"mul\((\d+),(\d+)\)", text)
    total += sum(int(a) * int(b) for a, b in matches)
    return total


# Read the input file
with open("input.txt") as f:
    content = f.read()

# Part 1: Total for all 'mul(a,b)' in the file
total = calc_mul_for_string(0, content)
print(total)

# Part 2: Total for 'mul(a,b)' in enabled blocks only
total = 0
enablers = content.split("do()")
for enabled_block in enablers:
    calc_block = enabled_block.split("don't()", 1)[0]
    total = calc_mul_for_string(total, calc_block)
print(total)
