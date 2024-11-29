import re


with open("input.txt", "r") as file:
    lines = file.read().splitlines()


def p(s):
    return s.split(' bags')[0].split('bag')[0]


map = {}
for l in lines:
    a, b = l.split('s contain ')

    out = []
    if 'no other' not in b:
        to = b[:-1].split(', ')
        for t in to:
            t = p(t)
            count = t.split(' ')[0]
            out.append((int(count), t[len(count)+1:].strip()))

    map[p(a).strip()] = out


count = -1
req = ['shiny gold']
while req:
    bag = req.pop()
    for a, b in map[bag]:
        req.extend([b] * a)
    count += 1

print(count)



exit()
short = {}
for a, b in map.items():
    short[a] = set([i[1] for i in b])


canget = {a: set(short[a]) for a in short}

for i in range(len(short)):
    print(i)
    for a, b in canget.items():
        n = set()
        for c in b:
            if c in short:
                # canget[a] += short[c]
                n = n.union(short[c])
                # canget[a].update(short[c])
            else:
                print('not', c)
        canget[a] = canget[a].union(n)


out = 0
for a, b in canget.items():
    if 'shiny gold' in b:
        print(a, b)
        out += 1

print(out)





