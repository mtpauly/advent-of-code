import re

L = open('input.txt', 'r').read().strip()

# part 1
total = 0
for i in range(len(L)):
    res = re.search('^mul\\((\\d+),(\\d+)\\)', L[i:])
    if res:
        total += int(res.groups()[0]) * int(res.groups()[1])

print(total)

# part 2
total = 0
enabled = True
for i in range(len(L)):
    if L[i:i+4] == 'do()':
        enabled = True
        continue
    if L[i:i+7] == "don't()":
        enabled = False
        continue

    res = re.search('^mul\\((\\d+),(\\d+)\\)', L[i:])
    if res:
        total += enabled * int(res.groups()[0]) * int(res.groups()[1])

print(total)
