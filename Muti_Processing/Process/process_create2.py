# _*_ coding:utf-8 _*_
from multiprocessing import Process
import time

class MyProcess(Process):

    def __init__(self, num:int):
        Process.__init__(self)
        self.num = num

    def hi(self):
        print('hello %s'% self.num)

    # 进程执行方法
    def run(self) -> None:
        self.hi()

if __name__ == '__main__':
    t1 = MyProcess(10) # 创建子进程
    t1.start()

    t2 = MyProcess(9) # 创建子进程
    t2.start()

    print('我是主进程...')