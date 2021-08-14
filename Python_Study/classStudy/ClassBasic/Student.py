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
    
    @classmethod
    def get_name(cls):
        return cls.__name

    # 将实例方法私有
    def __play(self):
        print("偷偷玩王者荣耀")

    def __del__(self):
        print("我被释放了")

def main():
    # print(dir(Student))
    # print(Student._Student__name) # 不推荐这种方式去访问
    # s = Student(1, "Python")
    # s._Student__play() # 不推荐这种方式去访问

    s = Student(1, "java")
    print(s.get_work())
    print(s.get_name())


    


if __name__ == '__main__':
    main()