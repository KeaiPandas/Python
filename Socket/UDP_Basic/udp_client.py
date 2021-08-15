# _*_ coding:utf-8 _*_
from socket import *

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

# 创建socket链接 SOCK_DGRAM -> udp协议
udp_client = socket(AF_INET, SOCK_DGRAM)

udp_client.sendto('hello', ip_port)

data, addr = udp_client.recvfrom(buffer_size)
print(data,addr)

udp_client.close()
