import requests

keyWord = input("enter a key word:")

url = 'https://www.sogou.com/web'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
params = {"query": "周杰伦"}
response = requests.get(url=url, headers=headers, params=params)
response.encoding = "utf-8"
page_text = response.text
fileNmae = keyWord + ".html"
with open(fileNmae, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print("爬取完毕")