from itertools import permutations as per

graph = 'FB FG GC BC BD CD AG AE DE'.split()
matrix = '45 345 256 127 123 37 46'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
