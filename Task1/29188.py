from itertools import permutations as per

graph = 'АБ АД АЖ ЖД ДЕ ЕК ИК ИЖ ГК ВГ БВ'.split()
matrix = '256 159 468 367 127 134 45 39 28'.split()

print(*range(1, 9))
for i in per('АБВГДЕИЖК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
