'''
#列表:存储多个元素的东西
b=[7,"fd",9]   #下标从0开始取值,列表元素可以替换,b[0]=1
#元组:存储多个元素的东西,元组里面的元素不可以重新赋值
c=(7,"fd",9)
#字典
#{键:值,键:值,...}
#取值格式:字典名["对应键名"]
a={"abc":7,"abcd":6,"d":8}
#集合
#集合:去重
e=set("fbadsjkfbdas")
b=set("fbayteyety")
g=e-b

#运算符+ -*/%
h=5+9*2-1
i=19%2
j="hello python"
#+可用来做字符串连接符
k="abc"+j

#if
a=22
b=1
if(19<a<21):
    print(a)
    if(b<9):
        print(b)
elif(a>10 and a<=19):
    print("a>9 and a<=19")
elif(a<9):
    print("a<9")        
else:
    print("python")

#while
a=0
while(a<10):
    print("python")
    a+=1
    
#for
#for:遍历列表
a=["aa","b","c","d"]
for i in a:
    print(i)
#for:进行常规循环
#for i in range(0,10)
for i in range(0,10):
    print("hello A")


#continue ,break
#break:全部直接退出,整个循环都中断
#continue:中断一次循环,继续下一次循环
for i in a:
    if(i=="c"):
        #break
        continue
    print(i)


#乘法口诀
#end="" 代表不换行输出
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
    print()

#逆向输出乘法口诀
for i in range(9,0,-1):
    for j in range(9,9-i,-1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
    print()

'''











