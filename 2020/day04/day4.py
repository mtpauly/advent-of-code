import re


with open("input.txt", "r") as file:
    lines = file.read().splitlines()


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


out = 0
p = []
for i, line in enumerate(lines + ['']):
    if i > 0 and not lines[i-1]:
        p = []

    if line:
        p.extend(line.split())
        continue

    if not line:
        p = {f[:3]: f[4:] for f in p}

        for f in fields:
            if f not in p:
                break

        else:
            try:
                byr = int(p['byr'])
                if byr > 2002 or byr < 1920:
                    continue
            except:
                continue

            try:
                iyr = int(p['iyr'])
                if iyr > 2020 or iyr < 2010:
                    continue
            except:
                continue
            
            try:
                eyr = int(p['eyr'])
                if eyr > 2030 or eyr < 2020:
                    continue
            except:
                continue

            hgt = p['hgt']
            if len(hgt) < 3:
                continue
            start = int(hgt[:-2])
            if hgt[-2:] == 'in':
                if start > 76 or start < 59:
                    continue
            elif hgt[-2:] == 'cm':
                if start > 193 or start < 150:
                    continue

            hcl = p['hcl']
            if len(hcl) != 7:
                continue
            if hcl[0] != '#':
                continue
            cont = False
            for c in hcl[1:]:
                if c not in 'abcdef0123456789':
                    cont = True
            if cont:
                continue

            ecl = p['ecl']
            if len(ecl) != 3:
                continue
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            pid = p['pid']
            if len(pid) != 9:
                continue
            cont = False
            for c in pid:
                if c not in '1234567890':
                    cont = True
            if cont:
                continue

            out += 1

print(out)
