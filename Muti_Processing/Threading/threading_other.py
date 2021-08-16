# _*_ coding:utf-8 _*_
import threading
import time

def listen():
    print('begin to lithen', time.strftime('%x'))
    time.sleep(3)
    print('end to listen', time.strftime('%x'))

def game():
    print('begin to game', time.strftime('%x'))
    time.sleep(5)
    print('end play game', time.strftime('%x'))

if __name__ == '__main__':
    t1 = threading.Thread(target=listen)
    t1.start()
    # print(t1.is_alive())
    # print(t1.getName())
    # t1.setName("我是子线程1")
    # print(t1.getName())

    print(threading.current_thread()) # 返回当前线程对象

    t2 = threading.Thread(target=game)
    t2.setDaemon(True) # 将子线程设置为守护线程
    t2.start()


    print('我是主线程')