!!!加空格
注释放需要注释的上面一行
注释符 # 后面需要空一格


''  "" 
''' '''可以保留数据格式,可换行


#三元操作符:x if 条件 else y
#断言:assert  关键词后面的条件为假死,程序自动崩溃,可以用来置入检查点,当需要确保程序中的某个条件为真时才能让程序正常工作
while 条件:
	循环体
for 目标(随便定义) in 表达式(列表[]or循环体):
	循环体

favourite="missmile"
for i in favourite:
	print(i,end="")
#range([start,] stop[,step=1])
#[]表示里面的参数可选
#step=1表示第三个参数的默认值是1
#range生成一个从start参数的值开始到stop参数的值结束的数字序列(不包含stop参数)
>>> for i in range(6):
	print(i)
	
0
1
2
3
4

>>> for i in range(0,7):
	print(i)

	
0
1
2
3
4
5
6
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9

#break 终止循环,并跳出循环
while True:
	if 条件:
		break
print()

#continue:终止本轮循环,并开始下轮循环,开始下一次循环前检验条件是否True
for 目标(随便定义) in 表达式(列表[]or循环体):
	if 条件判断:
		print()
		continue

>>> for i in range(10):
	if i%2 != 0:
		print(i)
		continue
	i +=2
	print(i)

	
2
1
4
3
6
5
8
7
10
9
#列表[]:可包含整数,浮点数,字符串,对象
member=[1,2.0,"sherLock",[1,2,3]]

#append():向列表添加元素,只能解释一个参数
#member.append()  .表示作用范围
>>> member.append("op")
>>> member
[1, 2.0, 'sherLock', [1, 2, 3], 'op']

#extend():用一个列表扩展另外一个列表
#member.extend([])
>>> member.extend(["临风花易落","miss"])
>>> member
[1, 2.0, 'sherLock', [1, 2, 3], 'op', '临风花易落', 'miss']

#insert():两个参数,第一个表示在列表中的位置,第二个表示插入的元素
>>> member.insert(0,"q-q")
>>> member
['q-q', 1, 2.0, 'sherLock', [1, 2, 3], 'op', '临风花易落', 'miss']

#remove():从列表中删除
>>> member.remove("miss")
>>> member
['q-q', 1, 2.0, 'sherLock', [1, 2, 3], 'op', '临风花易落']

#del语句 
>>> del member[1]
>>> member
['q-q', 2.0, 'sherLock', [1, 2, 3], 'op', '临风花易落']
#del member  删除整个列表

#pop() 去除列表中最后一个元素并返回值
>>> member.pop()
'临风花易落'
>>> member
['q-q', 2.0, 'sherLock', [1, 2, 3], 'op']
>>> name=member.pop()
>>> name
'op'
>>> member
['q-q', 2.0, 'sherLock', [1, 2, 3]]
>>> member.pop(0)
'q-q'
>>> member
[2.0, 'sherLock', [1, 2, 3]]

#列表的比较:只比较第0个的大小,后面不计
#列表可以相加,只能同元素相加,不能用于添加新元素
>>> list3=list1+list2
>>> list3
[123, 345, 234, 213]

>>> 123 in list3
True
>>> 123 not in list3
False

>>> list4=[123,["das","aaa"],234]
>>> list4
[123, ['das', 'aaa'], 234]
>>> "aaa" in list4                  #in只能判断一个层次的元素
False
>>> "aaa" in list4[1]           #选中列表中的列表进行判断
True
>>> list4[1][1]
'aaa'

dir(list) 可以查看list中可以使用的参数
>>> list3.count(123)  #count()计算出现次数
1
list.index(元素,起始位置,终止位置)   #返回元素第一次出现的位置

list.reverse()  #使list中的元素翻转
list.sort()     #使list中的元素从小到大排序
sort(reverse=False)  #sort默认排序由小到大,reverse=True,由大到小

list5=list1[:]与list6=list1结果不同  
#list6与list1指向同一个内存地址,list1改变,list6随之改变.而list5拷贝的结果是指向了另外一个内存,与list1相互独立

#元组:tuple
#不能被修改,创建元组的关键是要加逗号
>>> temp=(1,)
>>> temp
(1,)
>>> temp=1,
>>> temp
(1,)
>>> temp=()   #创建空元组
>>> temp
()

#字典
字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
无序的键=>值对集合
在同一个字典之内，关键字必须是互不相同。
 dict() 直接从键值对元组列表中构建字典
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
#字典推导
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

#字典遍历
#items()
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
# enumerate()
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
#zip()
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.



>>> temp=temp[:2]+("e",)+temp[2:]   #将元组切片,然后添加
>>> temp
('a', 'b', 'e', 'c', 'd')

capitalize():把字符串的第一个字符改成大写
>>> str1="xiaoxiao"
>>> str1.capitalize()
'Xiaoxiao'

casefold():将所有字符串的字符改为小写
center(width):将字符串居中,并使用空格填充至长度width的新字符串
>>> str2.center(30)
'           ERESdfsd           '

count(sub[,start[,end]]):返回sub在字符串里边出现的次数,start和end参数表示范围,可选

endswith(sub[,start[,end[]]]):检查是否以sub字符串结束,是返回True,否则flase

expandtabs([tabsize=8]):把字符串中的tab符号( \ t)转换为空格,不指定的话默认为8
>>> str3="i\tlove\t you"
>>> str3.expandtabs()
'i       love     you'

find(sub[,start[,end]]):在字符串中查找是否含有sub字符串,有返回索引值,没有返回-1

index(sub[,start[,end]]):和find类似,如果sub不在字符串中会产生异常值

isalnum():如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False

isalpha():如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False

isdeclma():如果字符串只包含十进制数字则返回True,否则返回False

isdigit():如果字符中只包含数字则返回True,否则返回False

islower():如果字符中至少包含一个区分大小写的字符,并且这些字符都是小写,则返回True,否则返回False

isnumeric():如果字符串中只包含数字字符,则返回True,否则返回False

isspace():如果字符串中只包含空格,则返回True,否则返回False

istitle():如果字符串是标题化(所有的单词都是以大写开始,其余字母均小写),则返回True,否则返回False

isupper():如果字符中至少包含一个区分大小写的字符,并且这些字符都是大写,则返回True,否则返回False

join(sub):以字符串作为分隔符,插入到sub中所有的字符之间
>>> str2.join("123")
'1ERESdfsd2ERESdfsd3'

ljust(width):返回一个左对齐的字符串,并使用空格填充至长度width的新字符串

lower():转换字符串中所有大写字符为小写

lstrip():去掉字符串左边所有空格
>>> str5="       io"
>>> str5
'       io'
>>> str5.strip()
'io'

partition(sub):找到字符串的sub,把字符串分成一个3元组(pre_sub,sub,fol_sub),如果字符串中不包含sun则返回("原字符串"," "," ")

replace(old,new[,count]:把字符串中的old子字符替换成new子字符串,如果count指定,则替换不超过count次
	>>> str3
'dsfdsaf'
>>> str3.replace("d","g")
'gsfgsaf'

rfind(sub[,start[,end]]):类似于find(),不过是从右边开始查找

rindex(sub[,start[,end]]):类似于index(),不过是从右边开始

rjust(width):返回一个右对齐的字符串,并使用空格填充至长度width的新字符串

rpartition(sub):类似于partition(),不过是从右边开始查找

rstrip():删除字符串末尾的空格

split(sep=None,maxsplit=-1):不带参数默认是以空格为分隔符切片字符串,如果maxsplit参数有设置,则仅分割maxsplit个字符串,返回切片后的子字符串拼接的列表
>>> str4="ioiodifhabifd"
>>> str4.split()
['ioiodifhabifd']
>>> str4.split("i")
['', 'o', 'od', 'fhab', 'fd']

splitlines(([keepends])):按照"\n"分离,返回一个包含各行作为元素的列表,如果keepends参数资费那个,则返回前keepends行

startswidth(prefix[,start[,end]]):检查字符串是否以prefix开头,是则返回True,否则返回False,start和end参数可以指定范围,可选

strip([chars]):删除字符串前边和后边所有的空格,chars参数可以定制删除的字符,可选
>>> str4="     ssssaaaa    "
>>> str4.strip()
'ssssaaaa'
>>> str4=str4.strip()
>>> str4
'ssssaaaa'
>>> str4.strip("a")
'ssss'

swapcase():翻转字符串中的大小写

title():返回标题化(所有的单词都是以大写开始,其余字母均小写)的字符串

translate(table):根据table的规则(可以由str.marketrans("a","b")定制),转换字符串中的字符
>>> str4
'ssssaaaa'
>>> str4.translate(str.maketrans("s","c"))    #将s转化为a
'ccccaaaa'

upper():转换字符串中所有小写字符为大写

zfill(width):返回长度为width的字符串,原字符串右对齐,前边用0填充

>>> "{0} love {1}.{2}".format("i","you","baby")
'i love you.baby'
#{}表示字段(0,1,2位置参数),i,you, baby传递给format,然后传递给0,1,2,进行格式化整理
>>> "{a} love {b}.{c}".format(a="i",b="you",c="baby")
'i love you.baby' 
#a,b,c为关键字参数
>>> "{0} love {b}.{c}".format("i",b="you",c="baby")
'i love you.baby'
#0为位置参数,b,c为关键字参数
>>> "{{0}}".format("不打印")  
'{0}'

>>> "{0:.1f}{1}".format(27.658,"GB")  #:在替换域中表示格式化符号的开始,.1表示四舍五入,保留一个小数点,f表示定点数
'27.7GB'

格式标记字符串 % 要输出的值组

%%	百分号标记 #就是输出一个%
%c	字符及其ASCII码
>>> '%c' % 97
'a'
>>> '%c %c %c'%(97,98,99)
'a b c'
%s	字符串
%d	有符号整数(十进制)
>>> '%d + %d = %d' % (4,5,4+5)
'4 + 5 = 9'
%o	无符号整数(八进制)
%x	无符号整数(十六进制)
%X	无符号整数(十六进制大写字符)
%e	浮点数字(科学计数法)
>>> '%e'%27.658
'2.765800e+01'
%E	浮点数字(科学计数法，用E代替e)
>>> '%E'%27.658
'2.765800E+01'
%f	浮点数字(用小数点符号)
>>> '%f'%27.658
'27.658000'
%g	浮点数字(根据值的大小采用%e或%f)
%G	浮点数字(类似于%g)



格式化操作符辅助指令
符号              作用
-           用做左对齐
>>> '%-8.2f'%73.4345
'73.43   '
+          在正数前面显示加号( + )
<sp>      在正数前面显示空格
#         在八进制数前面显示零('0'),在十六进制前面显示'0x'或者'0X'(取决于
          用的是'x'还是'X')
0        显示的数字前面填充‘0’而不是默认的空格
>>> '%010d'%5
'0000000005'
>>> '%-010d'%5
'5         '
%           '%%'输出一个单一的'%'
(var)    映射变量(字典参数)
m.n       m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
>>> '%8.2f'%73.4345
'   73.43'
>>> '%10d'%5

位运算符
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111

逻辑运算符
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'         5'

\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数yy代表的字符，例如：\o12代表换行
\xyy	十进制数yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出

Python Number 类型转换

int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串  


Python数学函数

函数	返回值 ( 描述 )
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根



Python随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python                             包含以下常用随机数函数：
choice(seq)	                       从序列的元素中随机挑选一个元素，比如random.choice(range(10))   从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])  从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
#>>> import random
#>>> random.randrange(9)
random()	                       随机生成下一个实数，它在[0,1)范围内
#random.random()
#或者
#>>> from random import random
#>>> random()
seed([x])	                       改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	                   将序列的所有元素随机排序
uniform(x, y)	                   随机生成下一个实数，它在[x,y]范围内

Python三引号（triple quotes）
python中三引号可以将复杂的字符串进行复制:
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
 >>> hi = '''hi 
there'''
>>> hi   # repr()
'hi\nthere'
>>> print hi  # str()
hi 
there


列表推导式
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
>>> vec = [2, 4, 6]
>>> [3*x for x in vec]
[6, 12, 18]
>>> [[x, x**2] for x in vec]
[[2, 4], [4, 16], [6, 36]]

>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]

>>> def myfirstfuction(name):
	'函数定义过程中的name是叫形参'
	#因为它只是一个形式,表示占据了一个参数位置
	print('传递进来的'+name+'叫作实参,因为它是具体的参数值')

	
>>> myfirstfuction("uu")
传递进来的uu叫作实参,因为它是具体的参数值
>>> myfirstfuction.__doc__    #__name__:函数中表示属性
'函数定义过程中的name是叫形参'


全局变量与局部变量
def discount(price,rate):
    final_price=price*rate
    old_price=50
    print("修改后的old_price1:",old_price)    # 局部变量值,存在于其他空间
    return final_price
old_price=float(input("请输入原价:"))
rate=float(input('请输入折扣率:'))
new_price=discount(old_price,rate)
print('修改后old_price的值是2:',old_price)    #全局变量值,存在于栈空间
print('打折后价格是;',new_price)
                                              #两个old_price存在于不同的空间
请输入原价:1000
请输入折扣率:0.9
修改后的old_price1: 50
修改后old_price的值是2: 1000.0
打折后价格是; 900.0


>>> fun1()
fun1正在被调用
>>> def fun1():
	print('fun1正在被调用')
	def fun2():
		print('fun2正在被调用')
	fun2()                       #内部函数整个作用域都在外部函数之内,只有在调用fun1时才能用fun2,不能再全局直接使用fun2  
                                #执行fun1,打印,执行fun2(),再运行fun2()函数,打印
	
>>> fun1()
fun1正在被调用
fun2正在被调用

闭包
>>> def funx(x):        
	def funy(y):
		return x*y
	return funy
#如果在一个内部函数里(funy()),对在外部作用域(非全局)(funx()整个函数)的变量(x)进行引用,内部函数(funy())就是一个闭包.
>>> i=funx(8)
>>> i
<function funx.<locals>.funy at 0x00000153064B38C8>
>>> i(5)
40
>>> funx(8)(5)
40


>>> def fun1():
	x=5
	def fun2():
		x*=x
		return x
	return fun2()       #返回fun2是在fun2函数内进行操作,此时x是一个外部变量,并没有在fun2中进行定义

>>> fun1()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    fun1()
  File "<pyshell#100>", line 6, in fun1
    return fun2()
  File "<pyshell#100>", line 4, in fun2
    x*=x
UnboundLocalError: local variable 'x' referenced before assignment
>>> def fun1():
	x=[5]
	def fun2():
		x[0]*=x[0]            #改成容器类型
		return x[0]
	return fun2()

>>> fun1()
25

>>> def fun1():
	x=5
	def fun2():
		nonlocal x         #nonlocal  声明x是一个非局部变量
		x*=x
		return x
	return fun2()

>>> fun1()
25


lambda [arg1 [,arg2,.....argn]]:expression
#冒号前面是参数,后边是返回值
#>>> def ds(x):
	return 2*x+1

>>> ds(5)
11
>>> x=lambda x:x*x+1
>>> x(5)
26

filter(function or None, iterable)
#形式为filter(None, iterable)将iterable中false的值过滤
>>> list(filter(None,[1,0,False,True]))#filter 返回一个对象
[1, True]

from…import 语句
#from modname import name1[, name2[, ... nameN]]
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377

From…import* 语句
#把一个模块的所有内容全都导入到当前的命名空间
import sound.effects.echo   #导入一个包里面的特定模块,必须使用全名去访问
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

#直接导入一个函数或者变量:
from sound.effects.echo import echofilter


#map()  映射
#两个参数,一个函数,一个可迭代序列
将序列的每一个元素,作为函数的参数进行运算加工,直到可迭代的序列每个元素加工完毕形成新的序列
>>> list(map(lambda x : x * 2,range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


递归
1.有调用函数自身的行为  2.有正确的返回条件
>>> def fun2(n):
	if n == 1:
		return 1
	else:
		return n * fun2(n-1)

	
>>> fun2(5)
120


#递归实现斐波那契数列,越大越慢
>>> def fun4(n):
	  if n < 1:
	    print("输入错误")
	    return(-1)
	  if n == 1 or n == 2:
	    return 1
	  else:
	    return fun4(n-2)+fun4(n-1)
#非递归实现
>>> def fun3(a):
	a1 = 1
	a2 = 1
	a3 = 1
	
	if a < 1:
		print ("输入错误")
		return -1
	while (a-2) > 0:
		a3 = a2 +a1
		a1 = a2
		a2 = a3
		a -= 1
	return a3


字典的内建方法:
dict.fromkeys(s[,v]),s字典的键值,v可选,没有定义返回	None
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict1.fromkeys((1,2,3),"number")
{1: 'number', 2: 'number', 3: 'number'}

keys:返回字典键的引用
>>> dict1
{0: 'a', 1: 'a', 2: 'a', 3: 'a', 4: 'a', 5: 'a'}
>>> for eachkey in dict1.keys():
	print(eachkey)

	
0
1
2
3
4
5
values:返回字典中的值
>>> for eachvalue in dict1.values():
	print(eachvalue)

	
a
a
a
a
a
a
items:返回每一项
>>> for eachitem in dict1.items():
	print(eachitem)

	
(0, 'a')
(1, 'a')
(2, 'a')
(3, 'a')
(4, 'a')
(5, 'a')

get:查询字典中的项,当没有时返回None
>>> print(dict1.get(7))
None
>>> dict1.get(7,"没有此项")
'没有此项'

clear:清空
>>> dict1.clear()
>>> dict1
{}

copy:copy之后指向不同的内存
>>> a={1:"one",2:'two',3:'three'}
>>> b=a.copy()
>>> c=a
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> b
{1: 'one', 2: 'two', 3: 'three'}
>>> id(a)
2163971301952
>>> id(b)
2163971062016
>>> id(c)
2163971301952

pop与popitem:字典中是无序的(字典是根据优先级排序),用popitem是随机的.pop返回一个键,popitem返回一个项
>>> a.pop(2)
'two'
>>> a.popitem()
(3, 'three')
>>> a
{1: 'one'}


setdefault:类似于get,在字典中没有找到时会自动添加
>>> a.setdefault("小白")
>>> a
{1: 'one', '小白': None}

update:利用一个字典或映射关系去更新一个字典
>>> b={"小白":"狗"}
>>> a.update(b)
>>> a
{1: 'one', '小白': '狗'}



set:集合,没有重复元素,可以用来筛选
num3=frozenset([1,2,3,4])   #不可更改的集合


文件读取
#file object = open(file_name [, access_mode][, buffering])
#file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
#access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
#buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
>>> s=open('G:\\Python36\\1.txt')
1	
file.close()

关闭文件。关闭后文件不能再进行读写操作。

2	
file.flush()

刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3	
file.fileno()

返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4	
file.isatty()

如果文件连接到一个终端设备返回 True，否则返回 False。

5	
file.next()

返回文件下一行。

6	
file.read([size])

从文件读取指定的字节数，如果未给定或为负则读取所有。

7	
file.readline([size])

读取整行，包括 "\n" 字符。

8	
file.readlines(seq)
向文件写入字符串序列seq,seq应该是一个返回字符串的可迭代对象


9	
file.seek（offset [,from]
#Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置
#如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
>>> s.seek(54,0)
54
#返回从头开始第54个字节后所在行
>>> s.readline()


10	
file.tell()

返回文件指针当前位置。

11	
file.truncate([size])

从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

12	
file.write(str)

将字符串写入文件，没有返回值。
写入之后要file.close之后才能在文件中显示写入的值,否则存在缓冲区里

13	
file.writelines(sequence)

向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

file.closed	返回true如果文件已被关闭，否则返回false。
file.mode	返回被打开文件的访问模式。
file.name	返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。

#将读取的文件转化为列表并读取
list(file)
>>> lines = list(s)
>>> s.seek(0,0)
0
>>> for each_line in s:
	print(each_line)