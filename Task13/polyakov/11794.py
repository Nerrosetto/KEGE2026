from ipaddress import *


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')


for A in range(0, 256)[::-1]:
    net = ip_network(f'233.167.{A}.167/255.255.255.192', False)
    if all(f(ip) for ip in net):
        print(A)
        break
