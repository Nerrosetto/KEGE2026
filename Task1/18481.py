from itertools import permutations as per

roads = 'AB AC BC BD EC DE DF FG EG'.split()
nume = '67 567 457 35 234 12 123'.split()

print(*range(1, 8))
for i in per('ABCDEFG'):
    if all(str(i.index(x) + 1) in nume[i.index(y)] for x, y in roads):
        print(*i)
