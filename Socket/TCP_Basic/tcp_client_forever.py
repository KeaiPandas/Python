# _*_ coding:utf-8 _*_
import socket

# 建立socket链接，socket.AF_INET是基于网络套接字家族 socket.SOCK_STREAM是tcp协议
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 买手机

# 与服务端建立链接
tcp_client.connect(('127.0.0.1', 8000)) # 拨号

while True:
    # 发消息给服务端
    msg = input('>>:').strip()
    if not msg:
        continue

    tcp_client.send(msg.encode('utf-8')) # 说话
    # 接受服务端的消息
    data = tcp_client.recv(1024) # 听消息，听话

    # 收到exit消息，中断链接
    if 'exit' == data.decode('utf-8'):
        print("与服务端断开连接")
        break
    print(data.decode('utf-8'))

# 断开与服务端的链接
tcp_client.close() # 挂电话