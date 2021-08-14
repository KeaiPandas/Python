# 异常处理: 自定义异常
# 需求： 模拟用户注册， 用户名必须为长度4～8, 且纯数字

'''
    1.用户输入注册信息
    2.判断是否为纯数字
    3.判断长度
    4.注册成功
'''
class CustomException(Exception):
    # 初始化对象属性
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 模拟注册
def register():
    # 1.用户输入注册信息
    str_name = input("请输入注册用户名信息")

    # 判断是否为空
    if 0 == len(str_name):
        raise CustomException("用户名不能为空")

    # 2.判断是否为纯数字
    flag = str_name.isdigit()

    if flag:
        # 3.判断长度4~8 如果表达式成立抛出异常123
        if 0 == len(str_name) or 3 >= len(str_name) or 9 <= len(str_name):
            raise CustomException("用户名不合法，请输入长度为4~8的用户名")
    else:
        raise CustomException("用户名不合法， 请输入纯数字的用户名")

    # 注册成功
    print("恭喜注册成功，用户名为:{}".format(str_name))

try:
    register()
except CustomException as e:
    print(f"程序异常了，异常信息为{e}")