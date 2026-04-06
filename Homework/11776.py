from ipaddress import *

cnt = 0
net = ip_network('235.86.56.0/255.255.248.0')
for ip in net:
    if f'{int(ip):032b}'[-2:] == '11':
        cnt += 1
print(cnt)
