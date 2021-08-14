# _*_ coding:utf-8 _*_


class House(object): #大驼峰
    area = 100 # 性别 1代表男 2代表女
    floor = 7   #   
    worth = 200 # 万人民币
    location = '上海松江'

    # 对象方法
    def  building(self):
        print("{}的房屋在修建".format(self.location))
    
    def help(self):
        print("拯救学习python和java的码农")

h = House()
h.color = '白色' # 对象属性
print(h.area)

House.area = 200

h1 = House()
print(h1.area)

h1.area = 100
print(h1.area)