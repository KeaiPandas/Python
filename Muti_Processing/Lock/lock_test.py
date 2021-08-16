# _*_ coding:utf-8 _*_
import threading
import time

def add():
    global num

    # 加锁是为了让锁内的资源无法共享，实现锁内的代码同步执行
    # 添加互斥锁，结果肯定为100,由原来的并发执行变成串行，牺牲了执行效率保证了数据安全
    _lock.acquire()
    temp = num
    time.sleep(0.01)
    num = temp + 1
    _lock.release() # 释放锁

if __name__ == '__main__':
    _lock = threading.Lock() # 创建互斥锁对象
    num = 0

    l = []
    
    for i in range(100):
        t = threading.Thread(target=add)
        t.start()
        l.append(t)
    
    for t in l:
        t.join()
    
    print(num)