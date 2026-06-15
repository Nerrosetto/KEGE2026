with open(r'Files/12241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if sorted([line.count(i) for i in set(line)]) == [1, 2, 2, 2]:
        a = [i for i in line if line.count(i) > 1]
        if sum([max(a), min(a)]) / 2 < [i for i in line if line.count(i) == 1][0]:
            cnt += 1
print(cnt)
