from re import finditer

with open(r'../17641/24_17641.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'
pattern = rf'({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    if eval(match) == 0:
        ans = max(ans, len(match))
    elif len(match) > ans:
        for d in range(len(match) - 1):
            if match[d] in '+*':
                continue
            if match[d] == '0' and match[d + 1] not in '+*':
                continue
            for r in range(len(match) - 1, d, -1):
                if match[r] in '+*':
                    continue
                new_match = match[d:r + 1]
                if new_match and eval(new_match) == 0:
                    ans = max(ans, len(new_match))
                    break
print(ans)
