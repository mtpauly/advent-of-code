from collections import defaultdict


L = open("input.txt", "r").read().splitlines()

mask = tuple(L[0].split()[-1])
mem = defaultdict(lambda: [0] * 36)

maskval = []

total = 0
for i, l in enumerate(L[1:]):
    if 'mask' in l:
        mask = tuple(l.split()[-1])
        continue

    if i + 1 != len(L) - 1 and 'mask' not in L[i+2]:
        continue

    a, b = l.split(' = ')
    idx = int(a.split('[')[-1][:-1]) #]
    num = int(b)

    total += 2**mask.count('X') * num

    for maskprev, valprev in maskval:
        one_overlap = 0
        two_overlap = 0
        for i in range(36):
            if maskprev[i] != 'X' and mask[i] != 'X':
                if maskprev[i] != mask[i]:
                    break
                else:
                    continue

            if maskprev[i] == 'X' and mask[i] == 'X':
                two_overlap += 1
                break
            
            one_overlap += 1
        else:
            total -= n_overlap * valprev


    maskval.append((mask, num))

print(maskval)
print(total)

    # val = []
    # for i in list(range(36))[::-1]:
    #     if 2**i <= num:
    #         val.append(1)
    #         num -= 2**i
    #     else:
    #         val.append(0)

    # val.extend([0] * (36 - len(val)))
    # val.reverse()

    # for i in range(36):
    #     if mask[i] == 'X':
    #         mem[idx][i] = val[i]
    #     else:
    #         mem[idx][i] = int(mask[i])
    
    # print(idx, val)
    # print(idx, mem[idx])
    # print()




# print(mask)
# print(mem[0])


# total = 0
# for val in mem.values():
#     s = 0
#     for i, n in enumerate(val[::-1]):
#         s += n * 2**i
#     total += s
#     # print(s, val)
