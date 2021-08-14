import sys

# 构建学生类
class Student(object):
    # 将类属性私有
    __name = '张三'
    __age = 18


    def __init__(self, sex, work) -> None:
        self.__sex = sex
        self.__work = work

    def get_work(self):
        return self.__work

    def set_work(self, work):
        self.__work = work
    
    @classmethod
    def get_name(cls):
        return cls.__name

    # 将实例方法私有
    def __play(self):
        print("偷偷玩王者荣耀")

    def __del__(self):
        print("我被释放了")

def main():
    # 使用内部机制修改
    s = Student(1, "java")
    s.set_work("Python")
    print(s.get_work())


if __name__ == '__main__':
    main()