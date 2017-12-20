'''
print('------------------我爱------------------')
temp=input("不妨猜一下我现在心中想的是哪个数字:")
guess=int(temp)
if guess == 8:
   print("wc,你猜对了")
    print("但是对了也没有奖励啊")
else:
    print("猜错了,现在想的是8啊")
print("game over") 

'''
#BIF(bulit-in functions):内置函数

'''

t=input("输入你的名字:")
print("你好,"+t)


'''

temp=input("输入1到100之间的数字:")
guess=int(temp)
if 0<guess<=100:
    print("nice")
else:
    print("wrong")
