'''
temp=input("猜一猜我现在想的数字:")
guess=int(temp)
if guess==8:
    print("你猜中了")
else:
    if guess>8:
        print("大了大了")
    else:
        print("小了小了")
print("game over")

'''

'''
temp=input("猜一猜我现在想的数字:")
guess=int(temp)
while guess !=8:
    temp=input("猜错了,继续猜吧:")
    guess=int(temp)
    if guess==8:
        print("你猜中了")
    else:
        if guess>8:
            print("大了大了")
        else:
            print("小了小了")
print("game over")

'''
import random
secret = random.randint (1,10)
temp=input("猜一猜我现在想的数字:")
guess=int(temp)
while guess !=secret:
    if guess>secret:
        print("大了大了")
    else:
        print("小了小了")
    temp=input("猜错了,继续猜吧:")
    guess=int(temp)
    if guess==secret:
        print("你猜中了")
print("game over")
