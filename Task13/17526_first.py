print('Решение 1:')
print('Количество нулей:', f'{192:b}'.count('0') + 8, '=>')
print('2**14 ==', 2 ** (f'{192:b}'.count('0') + 8) / 2)

print('#####' * 5)
print('Решение 2:')
from ipaddress import ip_network

net = ip_network('172.16.128.0/255.255.192.0')
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 2 != 0:
        cnt += 1
print(cnt)
