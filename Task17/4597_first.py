with open(r'.\Files\17_4597.txt') as file:  # . - переход на уровень выше, \ - нахождение файла.
    data = [int(x) for x in file]
ans = []
minn = min(data)
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]  # Также, можно так: num1, num2 = data[i:i+2] (data[0:2])
    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn
    if (u1 or u2) and any([u1, u2]) and u1 + u2 >= 1:
        ans.append(num1 + num2)
print(len(ans), max(ans))

################################################################

with open(r'.\Files\17_4597.txt') as file:
    data = [int(x) for x in file]
ans = []
minn = min(data)
for num1, num2 in zip(data, data[1:]): 
    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn
    if (u1 or u2) and any([u1, u2]) and u1 + u2 >= 1:
        ans.append(num1 + num2)
print(len(ans), max(ans))
