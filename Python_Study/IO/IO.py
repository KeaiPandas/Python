'''
input output Stream
四个步骤:
open
read
write
close
'''

def copy(src_path, end_path):
    # 读取流，写出流
    with open(src_path, "rb") as src:
        with open(end_path, "wb") as end:
            _size = 1024

            while True:
                data = src.read(_size)
                if not data:
                    break
                end.write(data)

src_path = "Python_Study/IO/IO.txt"
end_path = "Python_Study/IO/IO_Copy.txt"

copy(src_path, end_path)