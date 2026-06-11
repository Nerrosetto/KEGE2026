from itertools import permutations as per

matrix = '345 467 14 123567 14 24 245'.split()
graph = 'AG AF GF GE FE ED DG CD CG BC BG'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
