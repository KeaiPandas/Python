# _*_ coding:utf-8 _*_
from multiprocessing import Process
import time

def hi(num):
    print('hello %s'%num)
    time.sleep(3)

if __name__ == '__main__':
    # hi(10)
    t = Process(target=hi, args=(10,)) # 创建进程对象(子进程) Process-1
    t.start()

    t1 = Process(target=hi, args=(9,)) # 创建进程对象(子进程) Process-2
    t1.start()


    print('我是主进程...') # MainProcess