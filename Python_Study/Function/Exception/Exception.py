# 异常处理

def testExcept():
    print("程序正常执行")
    raise PermissionError("你懂得")

def test():
    try:
        testExcept()
    except Exception as a:
        print("处理异常的代码块")
        raise PermissionError("继续出错了...")
    finally:
        print("不管有没有异常我都执行")

test()