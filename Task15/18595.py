from itertools import combinations as combo


def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not (C or J)) <= (not A)


ans = []
line = [x + eps for x in range(48, 101) for eps in (0, 0.1, 0.9)]

for A1, A2 in combo(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

print('_' * 100)

line_A = [48, 83, 94, 100]
line_x = [60, 91, 97]

for A1, A2 in combo(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(max(ans))
