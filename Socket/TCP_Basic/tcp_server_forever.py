# _*_ coding:utf-8 _*_
import socket

# 建立socket链接，socket.AF_INET是基于网络套接字家族 socket.SOCK_STREAM是tcp协议
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 买手机

# 声明服务端的ip和端口
tcp_server.bind(('127.0.0.1', 8000)) # 绑定电话卡

back_log = 5
buffer_size = 1024

# 声明最大链接数
tcp_server.listen(back_log) # 待机

# 得到一个持续链接和客户端的地址
conn, addr = tcp_server.accept() # 接听电话
print(conn, addr)

# 内层循环，实现与客户端的永久交互
while True:
    # 接受客户端的消息
    data = conn.recv(buffer_size) # 听消息，听话
    if not data: break

    # 如果客户端发送exit, 中断连接
    if 'exit' == data.decode('utf-8'):
        conn.send(data)
        break

    print('客服端说：', data.decode('utf-8'))

    # 发送消息给客户端
    msg = input('>>:')
    conn.send(msg.encode('utf-8')) # 发消息，说话

# 断开与客户端的链接
conn.close() # 挂电话

# 关闭客服端
tcp_server.close() # 关机
