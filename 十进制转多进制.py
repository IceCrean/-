while True:
    number = input('请输入一个整数(输入Q退出程序)：')
    if number in ['q','Q']:
        break
    elif not number.isdigit():
        print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
        continue
    else :
            number = int(number)       
            print('十进制 --> 十六进制 ：%d -> 0x%x' %(number,number))
            print('十进制 -->   八进制 ：%d -> 0o%o' %(number,number))
            print('十进制 -->   二进制 ：%d ->'%number,bin(number))

