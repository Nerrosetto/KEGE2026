with open(r'../kege_25198501/files/task9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for pos, i in enumerate(data, start=1):
    if sorted([i.count(t) for t in set(i)]) == [1, 1, 1, 3]:
        if max(t for t in i if i.count(t) == 3) > sum(d for d in i if i.count(d) == 1) / 3:
            ans = pos
print(ans)
