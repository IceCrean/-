import requests   #网络请求
import re        #正则表达式模块
import urllib
import time
#网址   统一资源定位符
url='http://www.ximalaya.com/4932085/album/3160816?page=4'
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
html = requests.get(url,headers=head)# 请求网址
html.text#  反爬

html.status_code
re.findall('href="/4932085/sound/(.*?)/" hashlink title=',html.text)#(.*?)正则表达式,提取所有开头href="/4932085/sound/,结尾hashlink title=的网址
#循环得到所有网址
datas=[]   #空列表
for n in range(1,18):
    url='http://www.ximalaya.com/4932085/album/3160816?page='+str(n)
    html = requests.get(url,headers=head)
    data=re.findall('href="/4932085/sound/(.*?)/" hashlink title=',html.text)
    datas.extend(data)#把data中的数据加到datas中
list(set(datas))
#下载音乐
for m in list(set(datas)):
    time.sleep(2)
    js='http://www.ximalaya.com/tracks/'+m+'.json'
    a='http://www.ximalaya.com/tracks/19505515.json'
    html_1=requests.get(js,headers=head)
    m4a=html_1.json()['play_path_64']# 切片
    urllib.request.urlretrieve(m4a,'C:\\Users\\sherLock\\Desktop\\yy\\'+m+'.m4a')


html_1.json()['play_path_64']# 切片
