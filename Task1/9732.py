from itertools import permutations as per

graph = 'FC CG GA AD BD FB FC EF EB EC EG'.split()
matrix = '47 357 2567 16 236 345 123'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
