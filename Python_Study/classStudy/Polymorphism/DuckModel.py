# 多种形态
class Bird:

    def fly(self):
        print("鸟会飞")

class Pigeon(Bird):
    def fly(self):
        print("鸽子在飞")

class Parrot(Bird):
    def fly(self):
        print("麻雀在飞")

class Person():

    def fly(self):
        print("鸟人会飞")

def fly(bird):
    bird.fly()

p = Pigeon()
fly(p)
p1 = Parrot()
fly(p1)
p2 = Person()
fly(p2) # 鸭子模型