#异常处理
'''
异常处理格式
try:
    程序
except Exception as 异常名称:
    异常处理部分
'''
try:
    
    for i in range(0,10):
        print(i)
        if(i==4):
            print(fjadskl)
    print("hello")
except Exception as err:
    print(err)


#让异常后的程序继续,在局部进行.注意缩进
for i in range(0,10):
    try:
        print(i)
        if(i==4):
             print(fjadskl)
    except Exception as err:
        print(err)
print("hello")
