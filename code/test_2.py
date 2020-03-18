from lxml import html, etree
from bs4 import BeautifulSoup
import requests


def readHtmlSoup(url):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    request = requests.get(url, headers=headers)
    request.close()
    request.encoding = 'utf-8'
    html = request.text
    soup = BeautifulSoup(html, features='html.parser')
    return soup


def readHtmlText(url):

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    request = requests.get(url, headers=headers)
    request.close()
    request.encoding = 'utf-8'
    html = request.text
    return html




url = 'http://www.cnu.cc/works/389340'
#url="http://sc.chinaz.com/tupian/gudianmeinvtupian.html"
urlText = readHtmlText(url)
tree = html.etree.HTML(urlText)
divs=tree.xpath('//img[@class="bodyImg lazy"]/img')
print(divs)
for div in divs:
    imgurl=div.xpath('.//img/@src2')
    imgname=div.xpath('.//img/@alt')
    #print(imgname, imgurl)