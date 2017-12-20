'''
#作用域
i=10
def func():
    j=10
    print(j)
print(i)
func()

'''





'''
#函数定义的格式:
def 函数名(参数):
    函数体
''' 
def abc():               #定义函数
    print("fadshfkj")
#调用函数:函数名(参数)
abc()






#参数:与外界沟通的接口
#接口:形参和实参
#一般在函数定义的时候使用的参数是形参
#一般在函数调用的时候使用的参数是实参
def func2(a,b):
    if(a>b):
        print(str(a)+"比"+str(b)+"大")
    else:
        print(str(b)+"大于"+str(a)+"或者"+str(b)+"与"+str(a)+"相等")
func2(9,5)
func2(2,5)






'''
#模块的导入
#1.网络安装:cmd--pip--- pip install
#2.下载安装(whl):进入lfd python下载,在通过cmd,到相应文件夹,(pip install 文件全名)
#3.直接复制:要python和电脑版本相同才能复制,lib文件夹中

#自定义模块:把python保存到lib目录下

>>> import hello
>>> hello.hello()
hello python
>>> from hello import hello
>>> hello
<function hello at 0x00000188AE01B158>
>>> hello()
hello python
'''
import cgi    #导入cgi模块
cgi.closelog() #从cgi模块中调用closelog函数
from cgi import closelog  #调用cgi模块中的closelog函数
















