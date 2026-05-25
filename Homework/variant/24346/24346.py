with open(r'24346.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for pos, i in enumerate(data, start=1):
    if 1 < len(set(i)) < 8:
        a = sum(t for t in i if i.count(t) > 1) ** 2
        b = sum(t for t in i if i.count(t) == 1) ** 2
        if a > b:
            if sum(i) % 2 != 0:
                ans = pos
print(ans)
