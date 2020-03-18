import requests
from bs4 import BeautifulSoup as bs
import re

url = 'http://www.cnu.cc/works/389340'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}

pattern = re.compile(r'.*(?=\?width)')

res = requests.get(url,headers)
soup = bs(res.text, 'html.parser')
link = soup.find_all('img')
with open('./test.html', 'w') as f:
    f.write(res.text)
for pic in link:
    pic.find_all('a')
    imgurl = pic.get('src')
    r = re.match(pattern, imgurl)
    #print(imgurl)
    #print(r.group(0))
    #print(r)
print(res.text)
