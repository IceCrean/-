requests.post

form格式:
#form{'':''
#'':''
#'':''}
requests.post(url,data = form)

json格式:
import json
#json{'':''
#'':''
#'':''}
 s=json.dumps(json)
 requests.post(url,data = s)
 或者
 requests.request('post',url,data=s)
 或者
 requests.get(url,data = s)

 multipart格式:
files = {'file':open('文件名','rb')}

requests.post(url,files = files)