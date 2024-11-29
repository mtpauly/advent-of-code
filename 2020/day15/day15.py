from collections import defaultdict

# nums = [3, 1, 2]
nums = [9,19,1,6,0,5,4]

spokenon = defaultdict(lambda: [])
for i in range(len(nums)):
    spokenon[nums[i]] = [i+1]

last = nums[-1]

for i in range(len(nums)+1, 30000000 + 1):

    if len(spokenon[last]) == 1:
        num = 0
    else:
        num = spokenon[last][-1] - spokenon[last][-2]

    last = num
    spokenon[num].append(i)
    if len(spokenon[num]) > 2:
        spokenon[num] = spokenon[num][-2:]
    # print(i, num)

print(num)

