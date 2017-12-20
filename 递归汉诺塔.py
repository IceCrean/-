def han(n, x, y, z):
    if n == 1:
        print(x,'-->',z)
    else:
        # 将前n-1个盘子从x移动到y上
        han(n-1, x, z, y)
        # 将最底下的最后一个盘子从x移动到z上
        print (x, '-->',z)
        # 将y上的n-1个盘子移动到z上
        han(n-1,y, x, z)
n=int(input('汉诺塔层数:'))
han(n,'x', 'y', 'z')
