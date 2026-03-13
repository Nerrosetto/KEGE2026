from itertools import permutations as per

graph = 'АБ БВ БЕ БЖ ВЖ ЕЖ ЕД ЖГ ЖД ГЖ'.split()
matrix = '24567 146 5 12 1367 125 15'.split()
print(*range(1, 8))
for i in per('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
