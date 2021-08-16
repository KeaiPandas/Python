import queue
import threading
import time

q = queue.Queue()
def put():
    while True:
        q.put('first')
        q.put('second')
        q.put('third')
        time.sleep(5)

'''
结果（先进先出），会出现阻塞，get和put都会阻塞：
    put阻塞因为塞满了进不去
    get阻塞因为取空取不出来
'''
def get():
    while True:
        print(q.get())
        print(q.get())
        print(q.get())

if __name__ == '__main__':
    t1 = threading.Thread(target=put)
    t2 = threading.Thread(target=get)

    t1.start()
    t2.start()