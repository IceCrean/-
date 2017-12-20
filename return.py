return

>>> def sum(a,b):
	t=a+b
	print("函数内:",t)
	return t;
>>> print("函数外",sum(10,20))   #sum计算完之后将值返回sum(10,20),表示此时sum(10,20)=30,再完成print("函数外",sum(10,20))   
函数内: 30
函数外 30


>>> def sum(a,b):
	t=a+b
	print("函数内:",t)         
	return

>>> print("函数外",sum(10,20))      #return不带参数,返回None
函数内: 30
函数外 None


>>> def sum(a,b):
	t=a+b
	print("函数内:",t)

	
>>> print("函数外",sum(10,20))      #没有返回,即sun(10,20)在函数内计算完之后print,然后删除.返回none.
函数内: 30
函数外 None

在python中,任何函数都会有返回值,没有return参数就返回none