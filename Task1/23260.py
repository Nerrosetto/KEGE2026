from itertools import permutations as per

graph = 'DC CF FG GE EA AD HA HB HG BD BC'.split()
matrix = '346 348 12 127 678 15 458 257'.split()

print(*range(1, 9))
for i in per('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
