with open(r'../kege_25198499/files/task9.txt') as file:
    data = [int(i) for i in file]

a = max(i for i in data if abs(i) % 100 == 25)
cnt = 0

for nums in zip(data, data[1:], data[2:]):
    if [len(str(abs(i))) for i in nums].count(4) <= 2:
        if sum(nums) <= a:
            cnt += 1
print(cnt)
