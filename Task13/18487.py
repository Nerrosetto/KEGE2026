from ipaddress import *

for A in range(256):
    net = ip_network(f'192.214.{A}.184/27', False)
    if all(f'{int(ip):b}'.count('1') > 15 for ip in net):
        print(A)
        break

print('#' * 15)


# ИЛИ:

def f(ip):
    return f'{int(ip):032b}'.count('1') > 15


for A in range(256):
    net = ip_network(f'192.214.{A}.184/27', False)
    if all(f(ip) for ip in net):
        print(A)
        break
