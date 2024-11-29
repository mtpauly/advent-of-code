import math
L = open("input.txt", "r").read().splitlines()

x = 0
y = 0
wx = 10
wy = 1
dir = 'E'

move = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0), 
        'W': (-1, 0), 
        }

for l in L:
    act = l[0]
    num = int(l[1:])

    if act in ['N', 'S', 'E', 'W']:
        wx += num * move[act][0]
        wy += num * move[act][1]
    elif act == 'F':
        x += num * wx
        y += num * wy
    elif act == 'B':
        x += num * -wx
        y += num * -wy
    elif act == 'L':
        wxprime = wx * math.cos(math.radians(num)) - wy * math.sin(math.radians(num))
        wyprime = wy * math.cos(math.radians(num)) + wx * math.sin(math.radians(num))
        wx = wxprime
        wy = wyprime
    else:
        wxprime = wx * math.cos(-math.radians(num)) - wy * math.sin(-math.radians(num))
        wyprime = wy * math.cos(-math.radians(num)) + wx * math.sin(-math.radians(num))
        wx = wxprime
        wy = wyprime

print(x, y, abs(x)+abs(y))

