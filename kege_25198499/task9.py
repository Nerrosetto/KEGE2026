with open(r'../kege_25198499/files/task9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for pos, i in enumerate(data, start=1):
    if len(i) == len(set(i)):
        if (max(i) + min(i)) * 2 == (sum(i) - min(i) - max(i)) * 3:
            ans = pos
print(ans)
