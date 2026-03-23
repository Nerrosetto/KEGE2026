with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task26\Files\26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    delivery = [int(i) for i in file]

delivery = sorted(delivery)
ans = []
m = 1
for box in delivery:
    if sum(ans) + box <= S:
        ans.append(box)
        if box > m:
            m = box
a = ans[-1]
ans = ans[:-1]
free_space = S - sum(ans)
print(len(ans) + 1, max(i for i in set(delivery) if i <= free_space))
#              ^^^ добавляем 1, так как убрали одну коробку до этого.

ans.append(a)
free_space = S - sum(ans[:-1])
print(len(ans), max(i for i in set(delivery) if i <= free_space))
