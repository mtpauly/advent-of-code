with open("input.txt", "r") as file:
    L = file.read().splitlines()

N = [int(l) for l in L]

l = len(N)

# part 2
for i in range(l-1):
    for j in range(i, l):
        r = N[i:j+1]
        if sum(r) == 400480901:
            print(min(r) + max(r))

# part 1
for i, n in enumerate(N[25:]):
    has = False
    for j, a in enumerate(N[i: i+24]):
        for b in N[j+1:i+25]:
            if a + b == n:
                has = True
                break

    if not has:
        print(i, n)
        exit()



