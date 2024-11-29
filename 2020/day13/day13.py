L = open("input.txt", "r").read().splitlines()

start = int(L[0])
bus = L[1].replace('x', '').split(',')
bus = [(i, int(b)) for i, b in enumerate(bus) if b]


print(start)
print(bus)

# part 2 gave up
for i in range(1000000000):
    for j, b in bus:
        if (i + j) % b != 0:
            break
    else:
        print(i)
        break

# for i in range(start, 100000000):
#     for b in bus:
#         if i % b == 0:
#             print(b * (i - start))
#             exit()
#
