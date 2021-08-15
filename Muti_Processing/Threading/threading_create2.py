# _*_ coding:utf-8 _*_
import threading

class MyThread(threading.Thread):

    def __init__(self, num:int):
        threading.Thread.__init__(self)
        self.num = num

    def hi(self):
        print('hello %s'% self.num)

    # 线程执行方法
    def run(self) -> None:
        self.hi()

if __name__ == '__main__':
    t1 = MyThread(10) # 创建子线程
    t1.start()

    t2 = MyThread(9) # 创建子线程
    t2.start()

    print('我是主线程...')