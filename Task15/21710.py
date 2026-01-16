from itertools import combinations as combo


def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (not B and not C or C and B)


ans = []

line_A = [36, 60, 75, 110]
line_x = [59, 70, 90]

for A1, A2 in combo(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(min(ans))
