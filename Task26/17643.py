with open(r'../Task26/Files/26_17643.txt') as file:
    N = int(file.readline())
    goods = [list(map(int, i.split())) for i in file]

avg = sum(i[1] for i in goods) / N  # average
exp = {}  # expansive
for good in [good for good in goods if good[1] > avg]:
    if good[0] not in exp:
        exp[good[0]] = [not good[2], good[1], good[2]]
    else:
        exp[good[0]][0] += not good[2]
        exp[good[0]][2] += good[2]

exp = sorted(exp.values(), key=lambda x: (-x[0], -x[1], x[2]))[0]
print(exp[0] * exp[1], exp[2])
