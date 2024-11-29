import re


with open("input.txt", "r") as file:
    lines = file.read().splitlines()

out = 0
g = []
count = 0
for line in lines + ['']:
    if line:
        g.extend([c for c in line])
        count += 1
        continue

    for c in set(g):
        if g.count(c) == count:
            out += 1

    g = []
    count = 0

print(out)
