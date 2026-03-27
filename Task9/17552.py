with open(r'./Files/17552.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for nums in data:
    u1 = max(nums) < sum(nums) - max(nums)
    u2 = sorted([nums.count(i) for i in set(nums)]) == [1, 1, 2]
    if all((u1, u2)):
        cnt += 1

print(cnt)
