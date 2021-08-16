# _*_ coding:utf-8 _*_
import queue, time
import multiprocessing

def foo(q):
    time.sleep(1)
    print("son process")
    # 子进程put
    q.put(123)
    q.put("sxt")

if __name__ == '__main__':
    q = multiprocessing.Queue() # 进程队列对象
    p = multiprocessing.Process(target=foo, args=(q,)) # 创建子进程执行foo函数
    p.start()

    print("main process")
    # 主进程get
    print(q.get())
    print(q.get())