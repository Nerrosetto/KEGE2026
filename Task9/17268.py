with open(r'./Files/17268.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0

for i in data:
    if max(i) + min(i) <= sum(i) - (max(i) + min(i)):
        cnt += 1

print(cnt)
