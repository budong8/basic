# python 来完成request请求
# requests 第三方库

import requests

# get 请求 不带参数
# url = 'http://120.78.128.25:8765/index/login.html'
# res = requests.get(url)
# print(res)
# print("响应头：", res.headers)
# print("响应状态码：", res.status_code)
# print("响应正文：", res.text)  # 返回html文本内容（针对请求从服务器返回来的格式主要有html、xml、json）

# post请求带参数
# url_login = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
url_login= 'http://120.78.128.25:8765/Frontend/Index/login'
data = {'mobilephone': '18295715736', 'pwd': 'test123456'}
res = requests.post(url_login, data)
print('响应头', res.headers)
print('响应状态码', res.status_code)
print('响应文本', res.text, type(res.text))
print('响应json', res.json(), type(res.json()))
