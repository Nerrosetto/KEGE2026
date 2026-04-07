from itertools import permutations as per

graph = 'AF AB AD DF EF DC EC BC EG BG'.split()
matrix = '457 567 45 136 123 247 126'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    i = ''.join(i)
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
