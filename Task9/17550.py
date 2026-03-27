with open(r'./Files/17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for nums in data:
    u2 = False
    u1 = sorted([nums.count(t) for t in set(nums)]) == [1, 1, 1, 3]
    if u1:
        u2a = [t for t in nums if nums.count(t) != 1]
        u2b = [t for t in nums if nums.count(t) == 1]
        if sum(u2a) ** 2 > sum(u2b) ** 2:
            u2 = True
    if all((u1, u2)):
        cnt += 1

print(cnt)
