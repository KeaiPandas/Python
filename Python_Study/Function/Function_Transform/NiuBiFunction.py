from functools import reduce
# 高阶函数
def square(x):
    return x * x

r = map(square, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

r = map(str, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

def plus(x, y):
    return x + y

# reduce归约
r = reduce(plus, [1, 2, 3, 4])
print(type(r), r)

def paste_num(x, y):
    return x * 10 + y

r = reduce(paste_num, [1, 2, 3, 4, 5])
print(r)

# filter
def compare(x):
    return x < 20

r = filter(compare, [1,2,3,4,20,30])
print(list(r))