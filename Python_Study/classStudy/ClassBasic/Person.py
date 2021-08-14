import sys

# 构建人类
class Person(object):

    # 初始化对象属性
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    __slots__ = ("name", "age",)

# 对类无效
Person.sex = True
print(Person.sex)

# 对对象有效
p = Person("张三", 18)
# p.sex = True
# print(p.__dict__)