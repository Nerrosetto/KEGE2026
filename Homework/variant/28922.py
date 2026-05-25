from itertools import permutations as per

matrix = 'AB AH BC CD BG GC FD FE GE FH'.split()
graph = '47 458 67 125 246 35 138 27'.split()
print(*range(1, 9))
for i in per('ABCDEFGH'):
    if all(str(i.index(x) + 1) in graph[i.index(y)] for x, y in matrix):
        print(*i)
