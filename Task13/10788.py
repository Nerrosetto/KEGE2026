from ipaddress import *

ip_1 = ip_address(f'201.44.240.33')
ip_2 = ip_address(f'201.44.240.107')

cnt = 0
for mask in range(10, 32):
    net = ip_network(f'{ip_1}/{mask}', False)
    if all([i in net.hosts() for i in [ip_1, ip_2]]):
        if f'{int(net.network_address):032b}'.count('1') >= 5:
            cnt += 1
print(cnt)
