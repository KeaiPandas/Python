import random
import string

print(random.randint(10,100)) #不能加补偿
print(random.randrange(1,10,2)) #能加补偿
print(random.random())
print(random.choice('213123wadasdasd'))
print(random.sample('asdadaca',3))

print("".join(random.sample(string.digits+string.ascii_lowercase,5)))

a = list(range(100))
print(a)
random.shuffle(a)
print(a)