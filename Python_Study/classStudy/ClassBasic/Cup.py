
# 类：杯子
class Cup(object):
    # 类的属性
    m1 = 200

    # 定制方法
    def __init__(self, color, mat) -> None:
        print(id(self))
        self.color = color
        self.mat = mat


# 实例化对象
c = Cup('白色', '玻璃')
print(id(c))
# print(c.color, '--', c.mat)

c1 = Cup('黑色', '塑料')
print(id(c1))
# print(c1.__dict__)
# print(c1.color, '--', c1.mat)

def show_info(c:object) -> None:
    print(c.color, '--', c.mat)

show_info(c)
show_info(c1)