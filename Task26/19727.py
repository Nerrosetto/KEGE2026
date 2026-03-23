with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task26\Files\26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    delivery = [int(i) for i in file]

delivery = sorted(delivery)
ans = []
for bidon in delivery:
    if sum(ans) + bidon <= M:
        ans.append(bidon)
free_space = M - sum(ans[:-1])
cnt = len(ans)
for i in range(free_space)[::-1]:
    if max(ans) + i <= M and max(ans) + i in set(delivery):
        ans[-1] = max(ans) + i
        cnt += 1

print(len(ans), len([i for i in delivery if i > free_space]))
