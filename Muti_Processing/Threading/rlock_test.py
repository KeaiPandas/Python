# _*_ coding:utf-8 _*_
import threading
import time

class MyThread(threading.Thread):

    def actionA(self):
        _rlock.acquire()
        print(self.name, 'getA', time.strftime('%x'))
        time.sleep(2)

        _rlock.acquire()
        print(self.name, 'getB', time.strftime('%x'))
        time.sleep(1)
        _rlock.release()

        _rlock.release()

    def actionB(self):
        _rlock.acquire()
        print(self.name, 'getA', time.strftime('%x'))
        time.sleep(2)

        _rlock.acquire()
        print(self.name, 'getB', time.strftime('%x'))
        time.sleep(1)
        _rlock.release()

        _rlock.release()

    def run(self) -> None:
        self.actionA()
        self.actionB()

if __name__ == '__main__':
    _rlock = threading.RLock()

    l = []

    for i in range(5):
        t = MyThread()
        t.start()
        l.append(t)

    for t in l:
        t.join()

    print('ending...')