with open(r'task9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, i in enumerate(data, start=1):
    if sorted([i.count(t) for t in set(i)]) == [1, 1, 1, 2, 2]:
        a = sum([t for t in i if i.count(t) > 1])/4
        b = max([t for t in i if i.count(t) == 1])
        if a < b:
            print(pos)
            break
