from copy import deepcopy

L = open("input.txt", "r").read().splitlines()

L2 = ['.' * (len(L[0]) + 2)]
for l in L:
    L2.append('.' + l + '.')
L2.extend(['.' * (len(L[0]) + 2)])
L2 = [list(l) for l in L2]


def count_occ(r, c, li, p = False):
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue

            # for mult in [1]:
            for mult in range(1, 1000):
                if r+mult*dr == len(L) or r+mult*dr == 0:
                    break
                if c+mult*dc == len(L[0]) or c+mult*dc == 0:
                    break

                sq = li[r+mult*dr][c+mult*dc]
                if sq == '.':
                    continue
                total += sq == '#'
                if p:
                    print(dr, dc, mult, sq)
                break

    if p:
        print(total)
    return total


for i in range(1000):
    # print(i)

    L = deepcopy(L2)

    for r in range(1, len(L) - 1):
        # print()
        for c in range(1, len(L[0]) - 1):
            co = count_occ(r, c, L)
            # print(co, end='')
            if L[r][c] == 'L' and co == 0:
                L2[r][c] = '#'
            if L[r][c] == '#' and co >= 5:
                L2[r][c] = 'L'

    # print()
    # for l in L2:
    #     print(''.join(l))

    if L == L2:
        break

# count_occ(len(L)-1, 1, L2, True)
# count_occ(1, 1, L2, True)

total = 0
for l in L:
    total += sum([seat == '#' for seat in l])
print(total)

