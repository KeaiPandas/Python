# 函数： 返回函数

def outter(*args):
    print("外函数被调用")
    # 拼接字符串
    def inner():
        print("内函数被调用")
        print(";".join(map(str, args)))
    return inner

func = outter(1,2,3)
func()

# 递归：自己调用自己

def product(n):
    if n <= 0:
        return 1
    return product(n-1) * n

print(product(5))

'''
1 1 2 3 5 8 13 21
'''
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8), end=" ")