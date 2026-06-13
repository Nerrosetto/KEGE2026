from itertools import permutations as per

matrix = '24 134 267 125 47 37 356'.split()
graph = 'AG AF GF GE EB FC BC BD CD'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
