#2017-12-17
import requests   #网络请求模块
import time



#定义真实网址  统一资源定位符
url = 'https://api.live.bilibili.com/ajax/msg'

#要提交的数据

form = {'roomid':'5267615',
        'token':'',
        'csrf_token':''}
while True:


    time.sleep(2)
    #提交数据给url url返回弹幕
    html=requests.post(url,data = form)


    #返回json文件  提取数据,如果不是json文件,要用到正则

    content=list(map(lambda ii:html.json()['data']['room'][ii]['text'],range(10)))

    print(content)


print(html.json())
