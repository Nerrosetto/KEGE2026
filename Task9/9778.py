with open(r'./Files/9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    u1 = sorted([line.count(i) for i in set(line)]) == [1, 1, 1, 1, 2]
    u2 = False

    if u1:
        ne_pov = [i for i in line if line.count(i) == 1]
        pov = [i for i in line if line.count(i) != 1]
        u2 = pov[0] >= sum(ne_pov) / len(ne_pov)

    if all((u1, u2)):
        print(pos)
        break
