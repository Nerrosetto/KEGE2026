with open(r'Files/29962.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for pos, nums in enumerate(data, start=1):
    if sorted([nums.count(i) for i in set(nums)]) == [1, 1, 1, 1, 3]:
        a = [i for i in nums if nums.count(i) == 1]
        a = sum(nums) / len(nums)
        b = sum(i for i in nums if nums.count(i) == 3) / 3
        if a > b:
            ans = pos
print(ans)
