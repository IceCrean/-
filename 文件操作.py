#文件的操作
#打开
#open(文件地址,操作形式)
'''
w:写入
r:读取
b:二进制
a:追加
'''

fh=open("G:\\Python36\\1.txt","r")   #注意使用\\或者/

#文件读取
data=fh.read()
line=fh.readline()
x=0

#while True:
#    line2=fh.readline()
#    if(len(line)==0 and x>10):
#        break
#        print(line2)
#        x+=1
#fh.close()

#关闭文件
fh.close()

#文件的写入
data="一起学python."
fh2=open("G:\\Python36\\2.txt","w")
fh2.write(data)                          #写入data
fh2.close()                              #关闭
'''
fh2=open("G:\\Python36\\2.txt","w")
data2="学好python"
fh2.write(data2)                         #以w形式写入data2,覆盖原内容
fh2.close()
'''
data2="学好python"

fh3=open("G:\\Python36\\2.txt","a")      #以a或a+形式写入,在原内容后面添加新内容
fh3.write(data2)
fh3.close()




