import requests
import re

url = 'http://www.xiaohuar.com/list-1-%s.html'

for i in range(44):
    temp = url % i
    print(temp)
    #获取网页源码
    reponse = requests.get(temp)

    html = reponse.text


#从源码的文本里面匹配我们需要的图片的url
    img_urls = re.findall(r'/d/file/\d+/\w+\.jpg',html)#\d 匹配数字 \w匹配含数字字母的字符串
    for img_url in img_urls:
         img_reponse = requests.get('http://www.xiaohuar.com%s' % img_url )#获取图片的二进制信息
         print(img_url)
    #二进制信息
         img_data = img_reponse.content

    meizhi = img_url.split('/')[-1]
    with open('C:\\Users\\sherLock\\Desktop\\mz\\%s.jpg'% meizhi,'wb')as f:
        f.write(img_data)
