from itertools import combinations as combo


def f(x):
    A = A1 <= x <= A2
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    return C <= ((B and not A) <= (not C))


ans = []
line = [x + eps for x in range(54, 152) for eps in (0, 0.1, 0.9)]
for A1, A2 in combo(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))
