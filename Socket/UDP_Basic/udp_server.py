# _*_ coding:utf-8 _*_
from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

# 创建socket链接
udp_server = socket(AF_INET, SOCK_DGRAM)

# 绑定ip和端口
udp_server.bind(ip_port)

data, addr = udp_server.recvfrom(buffer_size)
print(data, addr)

udp_server.sendto()

udp_server.close()