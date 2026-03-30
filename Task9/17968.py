with open(r'./Files/17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    u1 = False
    u2 = False
    if max(nums) < sum(nums) - max(nums):
        u1 = True
    if sum([i for i in nums if i % 2 == 0]) == sum([i for i in nums if i % 2 != 0]):
        u2 = True
    if all((u1, u2)):
        cnt += 1
print(cnt)
