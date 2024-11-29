from copy import deepcopy

with open("input.txt", "r") as file:
    L = file.read().splitlines()

Lorig = deepcopy(L)
for i in range(len(L)):
    L = deepcopy(Lorig)

    if L[i][0] == 'n':
        L[i] = L[i].replace('nop', 'jmp')
    else:
        L[i] = L[i].replace('jmp', 'nop')

    seen = set()
    pos = 0
    acc = 0

    while True:
        if pos == len(L):
            print(acc)
            exit()

        if pos in seen:
            break

        seen.add(pos)

        op, n = L[pos].split()
        n = int(n)

        if op == 'jmp':
            pos += n
        elif op == 'acc':
            pos += 1
            acc += n
        else:
            pos += 1

