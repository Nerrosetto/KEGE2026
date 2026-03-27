with open(r'./Files/9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for pos, nums in enumerate(data, start=1):
    u1 = sorted([nums.count(i) for i in set(nums)]) == [1, 1, 1, 1, 3]
    u2a = [i for i in nums if nums.count(i) == 1]
    u2b = [i for i in nums if nums.count(i) != 1]
    u2 = sum(u2a) / len(u2a) <= u2b[0] if u2b else False
    if all((u1, u2)):
        cnt += 1
print(cnt)
