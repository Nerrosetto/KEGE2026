from ipaddress import *

net = ip_network(f'146.180.173.153/255.192.0.0', False)
print(net[-2])
print(max(net.hosts()))
print(str(max(net.hosts())).replace('.', ''))
