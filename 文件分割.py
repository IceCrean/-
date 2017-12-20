s = open('G:\\Python36\\1.txt')
#函数封装
def save_file(boy,girl,count):
    #文件的分割保存操作
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


boy = []
girl = []
for each_line in s:
    if each_line [:6] != "=======":
        #这里进行字符串分割操作
        (role,line_spoken) = each_line.split(":",1)
        if role == "b":
            boy.append(line_spoken)
        if role == 'g':
            girl.append(line_spoken)
        
    else:
        save_file(boy,girl,count)

        boy = []
        girl = []
        count += 1

save_file(boy,girl,count)

s.close()
        
