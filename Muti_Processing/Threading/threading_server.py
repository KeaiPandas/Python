# _*_ coding:utf-8 _*_
import socket
import threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('127.0.0.1', 8000))
socket.listen(5)

def tcp_server(conn):
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        conn.send(data.upper())

if __name__ == '__main__':
    while True:
        conn, addr = socket.accept()
        s = threading.Thread(target=tcp_server, args=(conn,))
        s.start()