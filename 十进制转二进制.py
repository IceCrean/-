denum =int( input("输入十进制数:"))
print (denum,"(10)",)
binnum = []
# 二进制数
while denum > 0:
    binnum.append(str(denum % 2)) # 栈压入
    denum //= 2
print ('= ',)
while len(binnum)>0:
    import sys
    sys.stdout.write(binnum.pop()) 
