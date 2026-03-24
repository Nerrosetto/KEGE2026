with open(r'./Files/9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []

for num, line in enumerate(data, start=1):
    u1 = False
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        u1 = True
    u2 = line.count(max(line)) == 1

    if all((u1, u2)):
        ans.append([num, sum(line)])

print(min(ans)[1])

############################

for num, line in enumerate(data, start=1):
    u1 = False
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        u1 = True
    u2 = line.count(max(line)) == 1

    if all((u1, u2)):
        print(sum(line))
        break
