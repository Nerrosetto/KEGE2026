with open(r'./Files/23268.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, nums in enumerate(data, start=1):
    u1 = sorted([nums.count(t) for t in set(nums)]) == [1, 1, 1, 2, 2]
    if u1:
        u2 = max([i for i in nums if nums.count(i) == 1]) > sum([i for i in nums if nums.count(i) != 1]) / len(
            [i for i in nums if nums.count(i) != 1])
    else:
        u2 = False
    if all((u1, u2)):
        print(pos)
        break
