import json

class God(object):
    pass

class Person(object):
    pass

class User2(Person, God, object):
    '''内置函数的理解'''

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}的年龄是:{self.age}"


def main():
    user = User2('张三', 18)
    print(user)

    # 实现序列化
    def ser(self):
        return self.__dict__

    user_dumps = json.dumps(user, default = ser, ensure_ascii = False)
    print(user_dumps)

    # 反序列化
    def hook(_dict):
        return User2(_dict['name'], _dict['age'])

    user = json.loads(user_dumps, object_hook=hook)
    print(user)

    # __doc__ 获取类的注释说明
    print(user.__doc__)

    # __name__ 打印类名
    print(User2.__name__)

    # __module__
    print(user.__module__)
    print(User2.__module__)

    # __base__
    print(User2.__bases__)

if __name__ == '__main__':
    main()