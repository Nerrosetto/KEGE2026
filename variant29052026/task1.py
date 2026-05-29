from itertools import product as pro, permutations as per

matrix = 'AH AD AE HG HB BC BD CD CF FG GE'.split()
graph = '346 348 12 127 678 15 458 257'.split()

print(*range(1, 9))
for i in per('ABCDEFGH'):
    i = ''.join(i)
    if all(str(i.index(x) + 1) in graph[i.index(y)] for x, y in matrix):
        print(*i)
