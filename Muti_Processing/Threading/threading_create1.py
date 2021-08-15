# _*_ coding:utf-8 _*_
import threading
import time

def hi(num):
    print('hello %s'%num)
    time.sleep(3)

if __name__ == '__main__':
    # hi(10)
    t = threading.Thread(target=hi, args=(10,)) # 创建线程对象(子线程) Thread-1
    t.start()

    t1 = threading.Thread(target=hi, args=(9,)) # 创建线程对象(子线程) Thread-2
    t1.start()


    print('我是主线程...') # MainThread