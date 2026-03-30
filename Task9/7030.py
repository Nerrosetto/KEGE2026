with open(r'./Files/7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    ans = [i for i in sorted(nums)]
    u1 = sorted([nums.count(i) for i in set(nums)]) == [2, 2, 2]
    u2 = False
    if ans[-1] == sum(nums[:1]) ** 0.5:
        u2 = True
    if all((u1, u2)):
        cnt += 1
print(cnt)
