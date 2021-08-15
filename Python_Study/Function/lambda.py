# lambda匿名函数
# 使用场景，逻辑简单，调用次数少

def echo():
    print("helloworld!")

f = lambda : print("hellowold")
f()

def sxt_sum(a, b):
    return a + b

num = lambda a,b:a + b
print(num(2, 5))