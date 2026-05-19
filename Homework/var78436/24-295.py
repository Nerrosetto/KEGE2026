# 7494

with open(r'../var78436/files/24-295.txt') as file:
    data = file.readline()

data = data.replace('DE',' ').split()
ans = 0
for i in range(len(data) - 240):
    line = 'DE'.join(data[i:i + 241])
    ans = max(len(line), ans)
print(ans)
