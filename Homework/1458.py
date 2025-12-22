from itertools import permutations as per

graph = 'ГА ГБ ГВ ГД ДЕ АБ АВ БД ВД БЕ ЕЖ ДЖ'.split()
matrix = '256 13467 2456 237 136 1235 24'.split()

print(*range(1, 8))
for i in per('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
