from itertools import permutations as per

graph = 'DF AF AB BC EC GE GD DE AC'.split()
matrix = '346 45 16 125 24 137 56'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
