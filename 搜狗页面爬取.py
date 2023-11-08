import requests

# 1,指定url
url = 'https://www.sogou.com/'
# 2,发起请求get方法的返回值为响应对象
response = requests.get(url=url)
# 3，获取响应数据
# .text：返回的是字符串形式的响应数据
page_text = response.text
# 4，持久化存储
with open('./sougou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
