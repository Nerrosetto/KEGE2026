maxi = -1
for x in range(1, 9431):
    cnt = 0
    num = 39 ** 483 + 39 ** 235 - x
    while num:
        if num % 39 == 0:
            cnt += 1
        num //= 39
    maxi = max(maxi, cnt)
print(maxi)

################################
ans = []
for x in range(1, 9430):
    num = 39 ** 483 + 39 ** 235 - x
    cnt = 0
    while num:
        if num % 39 == 0:
            cnt += 1
        num //= 39
    ans.append(cnt)

print(max(ans))
