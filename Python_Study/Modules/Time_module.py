import time

print(time.time())
print(time.localtime())
t1 = time.gmtime()

print(time.mktime(t1))

# time.sleep(3)
print("------")

print(time.asctime())
print(time.ctime(13333))

print(time.strftime("%Y-%M-%d",time.localtime()))