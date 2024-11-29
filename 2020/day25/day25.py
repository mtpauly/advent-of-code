L = open("input.txt", "r").read().splitlines()

n1 = 9789649
n2 = 3647239
mod = 20201227

# n1 = 5764801

def t(n, l):
    val = 1
    for _ in range(l):
        val *= n
        val %= mod
    return val

val = 1
for i in range(1, 1000000000000):
    val *= 7
    val %= mod
    if val == n1:
        size = i
        break

print(size)
print(t(n2, size))

