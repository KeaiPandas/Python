import sys

class User(object):

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

# 添加
u = User("张三", 10)
u2 = User("李四", 20)

_dict = {'name':'老王'}
# print('name' in u) # 不可以用in, in后面的变量必须可迭代
print('name' in u.__dict__)