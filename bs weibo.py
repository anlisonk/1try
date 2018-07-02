from bs4 import BeautifulSoup

soup = BeautifulSoup(open("E:/py3.5.1/bs4/weibo.html", 'rb').read().decode("utf-8"), "html.parser")

for ele in soup.find_all("a"):
    if len(ele.contents) > 0:
        print(ele.contents[0].encode("utf-8"))
    if "href" in ele.attrs:
        print(ele["href"].encode("utf-8"))
