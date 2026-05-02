with open(r'../Task26/Files/26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    astronauts = []
    for i in file:
        Id, e1, e2, e3, s = map(int, i.split())
        astronauts.append([sum((e1, e2, e3, s)), s, Id])

astronauts = sorted(astronauts, key=lambda x: (-x[0], -x[1], x[2]))

passed = astronauts[:K]
rejected = astronauts[K:]

half_score = passed[-1][0]

for astronaut in passed[::-1]:
    if astronaut[0] != half_score:
        print(astronaut[2])
        break
print(sum(1 for astronaut in astronauts if astronaut[0] == half_score))
