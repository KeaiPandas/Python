# _*_ coding:utf-8 _*_

# 经典版
class Angel(object): #大驼峰
    gender = 2 # 性别 1代表男 2代表女
    wing = '一对'
    king = '善良'

    # 对象方法
    def fly(self):
        print("忽隐忽现")
    
    def help(self):
        print("拯救学习python和java的码农")


angel = Angel()
print(type(angel))
print(dir(Angel))

# 与类无关的函数
def main():
    print(type(Angel))


# # 新式版
# class Angel(object):
#     gender = 2 # 性别 1代表男 2代表女
#     wing = '一对'
#     king = '善良'

#     # 对象方法
#     def fly(self):
#         print("忽隐忽现")
    
#     def help(self):
#         print("拯救学习python和java的码农")
