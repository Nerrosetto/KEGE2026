with open(r'Files/17_29349.txt') as file:
    data = [int(i) for i in file]

ans = []
mini = min(i for i in data if abs(i) % 123 == 0 and i > 0)
for nums in zip(data, data[1:]):
    if sum(nums) < mini:
        ans.append(sum(nums))

print(len(ans), max(ans))
