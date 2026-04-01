from math import prod

with open(r'./Files/24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    u1 = nums.count(max(nums)) == 1
    u2 = min(nums) not in (nums[0], nums[-1]) and max(nums) not in (nums[0], nums[-1])
    u3 = prod(sorted(nums)[-3:]) % min(nums) == 0
    u = sum((u1, u2, u3)) == 1
    if u:
        cnt += 1
print(cnt)
