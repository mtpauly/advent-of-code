L = open('input.txt', 'r').read().splitlines()

# part 1
total = 0
for l in L:
    nums = [int(i) for i in l.split()]
    direction = 1 if nums[1] > nums[0] else -1

    for a, b, in zip(nums[:-1], nums[1:]):
        if direction * (b - a) not in [1, 2, 3]:
            break
    else:
        total += 1

print(total)

# part 2
total = 0
for l in L:
    nums = [int(i) for i in l.split()]

    for i in range(len(nums)):
        nums_removed = nums[:i] + nums[i+1:]
        direction = 1 if nums_removed[1] > nums_removed[0] else -1

        for a, b, in zip(nums_removed[:-1], nums_removed[1:]):
            if direction * (b - a) not in [1, 2, 3]:
                break
        else:
            total += 1
            break

print(total)
