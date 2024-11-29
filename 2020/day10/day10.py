with open("input.txt", "r") as file:
    L = file.read().splitlines()

# part 1
n = [0] + sorted([int(l) for l in L])
n.append(n[-1] + 3)

diffsize = {1: 0, 2: 0, 3: 0}

for i in range(len(n)-1):
    diffsize[n[i+1]-n[i]] += 1

print(diffsize[1] * diffsize[3])

# part 2
get_to = {}
get_to[0] = 1

for i, val in enumerate(n):
    get_to[i] = 0
    if i > 0 and n[i] - n[i-1] <= 3:
        get_to[i] += get_to[i-1]
    if i > 1 and n[i] - n[i-2] <= 3:
        get_to[i] += get_to[i-2]
    if i > 2 and n[i] - n[i-3] <= 3:
        get_to[i] += get_to[i-3]
    get_to[0] = 1

print(get_to[len(L) - 1])

