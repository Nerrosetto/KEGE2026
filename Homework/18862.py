from ipaddress import ip_network as ip_n

net = ip_n('172.140.68.0/255.255.248.0', False)
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('0') > 15:
        cnt += 1
print(cnt)
