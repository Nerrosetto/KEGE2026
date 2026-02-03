from itertools import permutations as per

graph = 'AB AF AD FD FE EC DC BC EG BG'.split()
matrix = '457 567 45 136 123 247 126'.split()
print(*range(1, 8))
for t in per('ABCDEFG'):
    if all(str(t.index(x) + 1) in matrix[t.index(y)] for x, y in graph):
        print(*t)
