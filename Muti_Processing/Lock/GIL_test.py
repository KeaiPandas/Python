# _*_ coding:utf-8 _*_
import threading
import time

def add():
    sum = 0

    for i in range(10000000):
        sum += i
    print('sum', sum)

def mul():
    sum2 = 1
    
    for i in range(1,100000):
        sum2 *= i
    # print('sum2',sum2)

if __name__ == '__main__':
    start = time.time()

    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=mul)

    l = []
    l.append(t1)
    l.append(t2)

    # for t in l:
    #     t.start()
    
    # for t in l:
    #     t.join()

    add()
    mul()
    
    print('ending...')
    print('time %s'%(time.time()-start))

    