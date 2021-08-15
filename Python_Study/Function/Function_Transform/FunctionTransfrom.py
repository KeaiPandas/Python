# 传递函数
def recipe(*args):
    r = ["饼干", "蛋糕", "月饼", "雪糕"][len(args) - 1]
    return r

# 做糕点
def do_pastry(func, *args):
    print("做糕点," + func(*args))

do_pastry(recipe, "面粉")
do_pastry(recipe, "面粉", "奶油")
do_pastry(recipe, "面粉", "奶油", "五仁")
do_pastry(recipe, "面粉", "奶油", "五仁", "冰柜")
