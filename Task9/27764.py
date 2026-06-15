with open(r'Files/27764.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if len(set(i)) == len(i):
        if sum([max(i), min(i)]) * 2 == sum(i) - sum([max(i), min(i)]):
            ans += 1
print(ans)
