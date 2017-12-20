# 2017-12-17
import requests  # 网络请求模块  pip install requests

import time

# 定义真实网址  统一资源定位符   '     "    '''
url = 'https://api.live.bilibili.com/ajax/msg'

# 要提交的数据
form = {'roomid':'5267615',
'token':'',
'csrf_token':''}
# 提交数据给url  url返回弹幕



while True:


    time.sleep(2)

    html = requests.post(url,data = form)

    # json  正则  提取数据

   
    content =list(map(lambda ii:html.json()['data']['room'][ii]['text'],range(10)))

    print(content)