# _*_ coding:utf-8 _*_
import threading
import time

class Boss(threading.Thread):

    def run(self):
        print('今晚加班到22:00')
        _event.set() # 将等待线程的False状态修改为True

class Worker(threading.Thread):

    def run(self):
        _event.wait() # 默认值是False
        print('命苦')


if __name__ == '__main__':
    _event = threading.Event()

    t1 = Boss()
    t2 = Worker()

    t1.start()
    t2.start()

