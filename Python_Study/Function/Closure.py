# 函数嵌套函数
# 返回内函数
# 内函数引用外部函数的环境

def f():
    print("这是外函数")

    def g():
        print("这是内函数")
    
    return g

# 闭包:外部所使用到的参数不会被回收
def f(a):
    def g(b):
        def k(c):
            return a+b+c
        return k
    return g

t1 = f(1)
t2 = t1(2)
num = t2(3)
print(num)