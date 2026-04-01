from ipaddress import ip_network as ip_n

net = ip_n('214.187.224.0/255.255.224.0')
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    u1 = ip[-4:] == '1000'
    if ip.count('1') % 6 != 0 and u1:
        cnt += 1
print(cnt)
