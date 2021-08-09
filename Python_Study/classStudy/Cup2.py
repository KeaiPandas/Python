
# 类：杯子
class Cup2(object):
    # 类的属性
    m1 = 200

    # 定制方法
    def __init__(self, color, mat) -> None:
        print(id(self))
        self.color = color
        self.mat = mat
    
    def show_info(self) -> None:
        print(c.color, '--', c.mat)

    # 类方法
    @classmethod
    def show_info2(cls) -> None:
        print('这是一个类方法')

    # 静态方法
    @staticmethod
    def static_show_info():
        print('这是一个静态方法, 与类和方法无关')




# 实例化对象
c = Cup2('白色', '玻璃')


c1 = Cup2('黑色', '塑料')

Cup2.show_info2()
Cup2.static_show_info()