from ipaddress import ip_network

cnt = 0
net = ip_network('112.160.0.0/12')  # 12- количество единиц, которые есть в маске задачи.
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 3 != 0:
        cnt += 1
print(cnt)
