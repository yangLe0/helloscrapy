import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    # tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    tplt = "{0:^8}\t{1:{3}^8}\t{2:^3}"

    print(tplt.format("排名","学校名称","总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

# main()
def gen(n):
    #生成器写法
    for i in range(n):
        yield i ** 2
    #普通写法
    # ls = [i**2 for i in range(n)]
    # return ls

for i in gen(5):
    print(i, " ", end="")