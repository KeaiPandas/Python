# _*_ coding:utf-8 _*_
import socket
import threading

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('127.0.0.1', 8000))

while True:
    msg = input('>>: ').strip()
    if not msg: continue

    tcp_client.send(msg.encode('utf-8'))
    data = tcp_client.recv(1024)
    print(data)

tcp_client.close()

