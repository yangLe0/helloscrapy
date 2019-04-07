import requests
from bs4 import BeautifulSoup
# import os
r = requests.get("http://python123.io/ws/demo.html")

# print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser") #解析器
# print(soup)
# print(soup.find_all(string = "Basic Python"))

# print(soup.find_all('p','course'))
# print(soup.find_all(id='link1'))
import re
match = re.search(r'PY.*?N', 'PYANBNCNDN')
print(match.group(0))
# su = re.sub(r'[1-9]\d{5}',':zipcode', 'BIT 100081 TSU100084')
# print(su)
# for m in re.finditer(r'[1-9]\d{5}','BIT 100081 TSU100084'):
#     if m:
#         print(m.group(0))
# sp = re.split(r'[1-9]\d{5}','BIT 100081 TSU100084',maxsplit=1)
# print(sp)
# ls = re.findall(r'[1-9]\d{5}','BIT 100081 TSU100084')
# print(ls)
# m = re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
# print(m.string)
# print(m.re)
# print(m.pos)
# print(m.endpos)
# print(m.group(0))
# print(m.start())
# print(m.end())
# print(m.span())
# match = re.match(r'[1-9]\d{5}','BIT 100081')
# if match:
    # print(match.group(0))
# print(type(match))
# match = re.match(r'[1-9]\d{5}', '100081 BIT')
# if match:
#     print(match.group(0))
# print(soup.find_all(string = re.compile('python')))
# print(soup.find_all(id=re.compile('link')))
# print(soup.find_all('a'))
# print(soup.find_all('a',recursive=False))
# print(soup.find_all(['a','b']))
# for tag in soup.find_all(True): #所有标签名称被打印出来
#     print(tag.name)
# import re
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)
# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.a.prettify())

# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)
# print(soup.title.parent)
# print(soup.html.parent)
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])
# print("===========================")
# for sibling in soup.a.next_siblings:
#     print(sibling)
# print("===========================")
# for sibling in soup.a.previous_siblings:
#     print(sibling)

# print(soup.prettify())
# print(soup.title)
# tag = soup.a
# print(tag.attrs)
# print(tag.attrs['class'])
# print(type(tag.attrs))
# print(type(tag))
# print(tag.string)
# print(soup.p.string)
# print(type(soup.p.string))
# newsoup = BeautifulSoup("<b><!-- This is a comment--></b><p>This is not a comment</p>", "html.parser") #解析器
# print(newsoup.b.string)
# print(type(newsoup.b.string))
# print(newsoup.p.string)
# print(type(newsoup.p.string))
# url = "http://m.ip138.com/ip.asp?ip="
# try:
#     r = requests.get(url+'202.204.80.112')
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[-500:])
# except:
#     print('爬取失败')
# url = "http://img0.dili360.com/pic/2019/02/15/5c667b0681c3f1q37878148_t.jpg"
# root = "D:/pics/"
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         # print(r.status_code)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print('文件保存成功')
#     else:
#         print('文件已存在')
# except:
#     print('爬取失败')
# r = requests.get("https://item.jd.com/2967929.html")
# r = requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y')
# print(r.status_code)
# print(type(r))
# print(r.headers)
# print(r.encoding)
# print(r.request.headers)
# kv = {'User-Agent': 'Mozilla/5.0'}
# kv = {'User-Agent': '*'}
# url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
# kv = {'wd':'Python'}
# r = requests.get("http://www.baidu.com/s", params = kv)
# print(r.status_code)
# print(r.request.headers)
# print(r.headers)
# print(r.request.url)
# print(len(r.text))
# print(r.apparent_encoding)
# r.encoding = 'utf-8'
# print(r.text[:1000])
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

# if __name__ == "__main__":
    # url = "www.baidu.com"
    # print(getHTMLText(url))
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.post('http://httpbin.org/post', data = payload)
    # r = requests.post('http://httpbin.org/post', data = 'ABC')
    # print(r.text)
    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.request('POST','http://python123.io/ws',json = payload)
    # body = 'ffff'
    # r = requests.request('POST','http://python123.io/ws',data = body)
    # hd = {'user-agent': 'Chrome/10'}
    # r = requests.request('POST','http://python123.io/ws',headers = hd)
    # fs = {'file': open('data.xls', 'rb')}
    # r = requests.request('POST','http://python123.io/ws',files = fs)
    # r = requests.request('GET','http:/www.baidu.com',timeout = 10)
    # pxs = {'http': 'http://user:pass@10.10.10.1"1234','https':'https://10.10.10.1:4321'}
    # r = requests.request('GET','http:/www.baidu.com',proxies = pxs)

