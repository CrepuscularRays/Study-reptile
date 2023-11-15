import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/doulist/134462233/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

index = 0
while 1:
    if index > 225:
        break
    params = {"start": str(index)}
    response = requests.get(url=url, headers=headers, params=params)
    response.encoding = "utf-8"
    page_text = response.text
    soup = BeautifulSoup(page_text, "html.parser")
    allTitles = soup.findAll("div", attrs={"class": "title"})
    title_list = []
    all_abs = soup.findAll("div", attrs={"class": "abstract"})
    for title in allTitles:
        for i in str(title).split("\n"):
            if "<" not in i:
                title_list.append(i.strip())

    num = 0
    for abs in all_abs:
        movie_string = f"排名：{index + num + 1}\n电影名称："
        movie_string += title_list[num] + "\n"
        for i in str(abs).split("\n"):
            if ("<" not in i) and (not i.isspace()):
                movie_string += i.strip() + "\n"
        num += 1
        movie_string += "\n"
        with open("豆瓣top250.txt", "a", encoding="utf-8") as f:
            f.write(movie_string)
    index += 25
