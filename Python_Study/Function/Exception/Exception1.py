# 异常处理： 通过健壮性
# 判断一个人的年龄，大于18岁提醒戒烟，小于18告诉他未成年不允许吸烟

def testExcept(str_age):
    # 判断是否是整数
    flag = (type(1) == type(str_age)) # False说明是字符串

    # 判断是否为字符串
    if not flag:
        flag = (type(1) == type(str_age)) and str_age.isdigit() #判断字符串是否为整数
    
    if flag:
        age = int(str_age)

        if age > 18:
            print("吸烟有害健康")
        else:
            print("未成年不允许吸烟")
    else:
        print("非法格式")

testExcept("dsadas")