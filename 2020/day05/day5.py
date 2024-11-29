import re


with open("input.txt", "r") as file:
    lines = file.read().splitlines()

all = []
for i in range(128):
    for j in range(8):
        all.append((i, j))

vals = []
for line in lines:
    row = line[:-3]
    col = line[-3:]

    def find(s, m):
        rmin = 0
        rmax = m - 1

        for char in s:
            diff = rmax - rmin + 1
            assert diff % 2 == 0
            if char == 'F' or char == 'L':
                rmax -= diff // 2
            else:
                rmin += diff // 2

        assert rmin == rmax
        return rmin

    r = find(row, 128)
    c = find(col, 8)
    print(r, c)
    all.remove((r, c))

    vals.append(r * 8 + c)

print(all)
print(max(vals))
