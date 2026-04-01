from math import prod

with open(r'./Files/24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    if nums.count(max(nums)) == 1:
        if max(nums) not in [nums[0], nums[-1]] and min(nums) not in [nums[0], nums[-1]]:
            if prod(sorted(nums)[-3:]) % min(nums) == 0:
                cnt += 1
print(cnt)
