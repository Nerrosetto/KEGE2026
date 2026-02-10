from itertools import combinations as combo


def f(x):
    return ((160 <= x <= 250) <= (10 <= x <= 150)) or ((not (A1 <= x <= A2)) <= (240 <= x <= 300))


ans = []
line_A = [10, 150, 160, 240, 250, 300]
line_x = [50, 155, 175, 245, 275]

for A1, A2 in combo(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(min(ans))
