with open(r'Files/29341.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if max(i) < sum(i) - max(i):
        if i[0] + i[1] != i[2] + i[3]:
            if i[1] + i[3] != i[2] + i[0]:
                if i[1] + i[2] != i[0] + i[3]:
                    ans += 1
print(ans)
