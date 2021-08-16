# _*_ coding:utf-8 _*_
from multiprocessing import Process
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
    t1 = Process(target=listen)
    t1.start()
    # t1.join() # 相当于没有意义
    # t1.join() # 相当于没有意义

    t2 = Process(target=game)
    t2.start()

    # t1.join()
    # t2.join()

    print('我是主线程')