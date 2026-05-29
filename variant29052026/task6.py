from itertools import product as pro

answer = 0
for pos, i in enumerate(pro(sorted('СТРОКА'), repeat=5), start=1):
    i = ''.join(i)
    if pos % 2 != 0 and i[0] not in 'АЛ' and i.count('С') == 1:
        answer = pos
print(answer)
