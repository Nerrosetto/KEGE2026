from ipaddress import *

cnt = 0
net = ip_network('214.96.0.0/255.240.0.0', False)
for ip in net:
    if f'{int(ip):032b}'.count('0') % 3 == 0:
        cnt += 1
print(cnt)
