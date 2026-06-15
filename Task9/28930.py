with open(r'Files/28930.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if i[0] < i[1] < i[2] < i[3] < i[4]:
        if min(i) + max(i) <= sum(i) - (min(i) + max(i)):
            ans += 1
print(ans)
