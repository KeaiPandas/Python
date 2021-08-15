from io import StringIO

# StringIO读取 wirte()写入内存 getvalue()获取内存
with StringIO(r"Python_Study/IO/IO.txt") as sio:
    len = sio.write("hello world") # 将内容写入内存中， 返回写入的个数

    data = sio.getvalue() # 从内存获取内容
    print(data)

# 其他写法
sio = StringIO()
len = sio.write("hello World")
data - sio.getvalue()
print(data)