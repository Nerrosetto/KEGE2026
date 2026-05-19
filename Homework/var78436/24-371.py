# 8835

from re import finditer

# with open(r'../var78436/files/24-371.txt') as file:
#     data = file.readline()

# re:
# pattern = r'([^M\.]*M){112}[^M\.]*\.'
# matches = [match.group() for match in finditer(pattern, data)]
# print(len(max(matches, key=len)))

# zamena1:

# data = data.split('M')
# ans = 0
# for i in range(len(data) - 112):
#     line_1 = data[i]
#     line = 'M' + 'M'.join(data[i + 1:i + 112]) + 'M'
#     line_113 = data[i + 112]
#     if line.count('.') != 0 or line_113.count('.') == 0:
#         continue
#     if '.' in line_1:
#         line_1 = line_1[line_1.rfind('.') + 1:]
#     line_113 = line_113[:line_113.find('.') + 1]
#     line = line_1 + line + line_113
#     ans = max(len(line), ans)
# print(ans)

with open(r'../var78436/files/24-371.txt') as file:
    data = file.readline()

# zamena2:

data = data.replace('.', '.#')
data = data.split('#')[:-1]

ans = 0
for line in data:
    count_M = line.count('M')
    if count_M == 112:
        ans = max(len(line), ans)
    elif count_M > 112:
        while count_M > 112:
            if line[0] == 'M':
                count_M -= 1
            line = line[1:]
        ans = max(len(line) + 2, ans)
print(ans)
