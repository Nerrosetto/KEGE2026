from ipaddress import *


# for mask in range(24, 31):
#     net = ip_network(f'172.16.168.0/{mask}', False)
#     cnt = 0
#     for ip in net:
#         ip = f'{int(ip):032b}'
#         if ip.count('0') % 7 == 0:
#             cnt += 1
#     if cnt == 35:
#         print(net.netmask)

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('0') % 7 == 0


for mask in range(24, 31):
    net = ip_network(f'172.16.168.0/{mask}', False)
    if sum(f(ip) for ip in net) == 35:
        print(net.netmask)
