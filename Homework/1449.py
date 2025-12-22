from itertools import permutations as per

graph = 'АБ АВ БВ ВД ВГ ВЕ ГЕ ГК ЕК ЕД'.split()
matrix = '24 146 56 1267 36 23457 46'.split()

print(*range(1, 8))
for i in per('АБВГДЕК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
