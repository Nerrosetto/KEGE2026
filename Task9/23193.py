with open(r'./Files/23193.txt') as file:
    data = [list(map(int, i.split())) for i in file]

pos = len(data)
for nums in data[::-1]:
    u1 = sorted([nums.count(i) for i in set(nums)]) == [1, 1, 1, 3]
    if u1:
        u2 = [i for i in nums if nums.count(i) != 1][0] > sum([i for i in nums if nums.count(i) == 1]) / len(
            [i for i in nums if nums.count(i) == 1])
    else:
        u2 = False
    if all((u1, u2)):
        print(pos)
        break
    else:
        pos -= 1
