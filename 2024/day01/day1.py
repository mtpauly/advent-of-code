L = open('input.txt', 'r').read().splitlines()

left, right = [], []
for l in L:
    a, b = l.split()
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()

# part 1
total = 0
for a, b in zip(left, right):
    total += abs(b-a)
print(total)

# part 2
total = 0
for a in set(left):
    total += a * right.count(a)
print(total)
