from itertools import permutations as per

graph = 'AF AE FD FC ED EH BH HG BD GC FC'.split()
matrix = '367 568 18 58 47 127 56 234'.split()

print(*range(1, 9))
for i in per('ABCDEFHG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
