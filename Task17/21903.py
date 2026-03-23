with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_21903.txt') as file:
    data = [int(i) for i in file]
ans = []
b = min(i for i in data if abs(i) % 100 == 15 and len(str(abs(i))) == 3)
for nums in zip(data, data[1:], data[2:]):
    u1 = False
    u2 = False
    cnt = 0

    for i in nums:
        if i > 0:
            cnt += 1
        else:
            cnt -= 1
    if cnt == 3 or cnt == -3:
        u1 = True

    a = min(nums) * max(nums)
    if a > b**2:
        u2 = True

    if all((u1, u2)):
        ans.append(min(nums) * max(nums))
print(len(ans), min(ans))
