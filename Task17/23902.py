with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task17\Files\17_23902.txt') as file:
    data = [int(t) for t in file]
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u = sum((str(num1)[0] == str(num1)[-1],
             str(num2)[0] == str(num2)[-1],
             str(num3)[0] == str(num3)[-1]))
    c = sum(((len(str(num1)) == 4 and str(num1)[1] == '2'), (len(str(num2)) == 4 and str(num2)[1] == '2'), (
            len(str(num3)) == 4 and str(num3)[1] == '2')))
    if all((u == 1, c == 2)):
        ans.append(max(num1, num2, num3))
print(len(ans), sum(ans))
