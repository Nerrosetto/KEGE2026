from re import sub

with open(r'../Files/24_14510.txt') as file:
    data = file.readline()
data = sub(r'[^EYUIOA]{2}[EYUIOA]', '*', data)

data = data.split('*')
ans = len(data) ** 2
for i in range(1, len(data) - 498):
    line = '***' + '***'.join(data[i:i + 499]) + '***'
    ans = min(len(line), ans)
print(ans)
