with open(r'./Files/Task9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, nums in enumerate(data, start=1):
    if [nums.count(i) for i in set(nums)] == [1, 1, 1, 1, 2]:
        a = [i for i in nums if nums.count(i) > 1]
        a = sum(a) / len(a)
        if a >= sum(i for i in nums if nums.count(i) == 1) / 4:
            print(pos)
            break
