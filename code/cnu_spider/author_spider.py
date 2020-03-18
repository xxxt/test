import os
from time import sleep,time
from threading import Thread

import requests
from lxml import etree
from time import sleep,time
import re
import csv
# import json
# import pymysql
# from DBUtils.PooledDB import PooledDB


# csv_headers = ['work','work_url','author','author_url','category','img_url','upload_time']

# MYSQL_HOST = 'localhost'
# USER = 'root'
# PASSWORD = '12345678'
# DB = 'cnu'
# PORT = 3306

# pool = PooledDB(pymysql, 5, host=MYSQL_HOST, user=USER, passwd=PASSWORD, db=DB, port=PORT) 
# con = pool.connection()

class DownloadTask(Thread):

    def __init__(self,data):
        super().__init__()
        self.data = data

    def run(self):
        path = self.data['title']
        if not os.path.exists('./img/'+path):
            os.mkdir('./img/'+path)

   

        for img_url in self.data['img_url']:

            name = img_url.split('?')[0].split('/')[-1]
            try:
                image = requests.get(img_url)
            except ConnectionError:
                sleep(5)
                image = requests.get(img_url)
            except:
                print('Error in ' + self.data['title'] + ': ' + name)
                # error_url.append(img_url)
            
        
            with open('./img/'+path+'/'+name, 'wb') as f:
                f.write(image.content)
                #print('save complete:{}'.format(name))
                f.close()
    
def get_work_data(work_url):
    payload = {}
    img_url = []
    data = {}

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://www.cnu.cc/users/255998',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    # 'Cookie': 'Hm_lvt_debc91213222aae0abfdb6176ec8d28a=1582887234,1582968419,1583072953,1583072998; laravel_session=eyJpdiI6IkhnZTVnczRnNVlvZUtPMFRhTEprVkE9PSIsInZhbHVlIjoiQ3JRY3JGaGxNSDl2ck0rbDRIcU9aOTI1UjFPTUdlSUM0MitSSGZMK256cnE2RjVWa0Z6bHJrWjBoa1pBaCtyb0JEQ0RSQWNSMk9wVHZBVzNPM0N4OVE9PSIsIm1hYyI6IjJjNzUwMjRmMWRkMzI1YTg4YWM5ODg5Zjg1MTllYzBmZTM5MDE0Yzc1Y2NhYzMzYWNhYWEwNDBmM2Y4MjFlOWQifQ%3D%3D; Hm_lpvt_debc91213222aae0abfdb6176ec8d28a=1583210175'

    def get_data(work_url):

        
        response = requests.request("GET", work_url, headers=headers, data=payload)

        source = response.text
        html = etree.HTML(source)

    
        title = html.xpath('normalize-space(/html/body/div[1]/div[2]/h2/text())')
        author = html.xpath('normalize-space(/html/body/div[1]/div[2]/span/a/strong/text())')
        upload_time = html.xpath('normalize-space(//*[@class="author-info"]/span/text())')
        author_url = (html.xpath('normalize-space(/html/body/div[1]/div[2]/span/a/@href)'))
        count = html.xpath('normalize-space(/html/body/div[1]/div[2]/div/span[2]/span/text())')
        category = html.xpath('/html/body/div[4]/div/div/div[1]/div[1]/a/text()')
    
        lists = html.xpath('normalize-space(//*[@id="imgs_json"])')
        d = re.findall(r'(?<=img":")\d+/\d+/\w+.jpg', lists)
        for j in d:
            img_url.append('http://imgoss.cnu.cc/'+j)
        # for i in lists:
        #     for j in json.loads(i):
        #         img_url.append('http://imgoss.cnu.cc/'+j['img'])


        data['author'] = author
        data['title'] = title
        data['work_url'] = work_url
        data['author_url'] = author_url
        data['upload_time'] = upload_time
        data['count'] = count
        data['img_url'] = img_url
        data['category'] = category

        return data


    try:
        get_data(work_url)
    except ConnectionError:
        sleep(5)
        get_data(work_url)
    except:
        with open('./log', 'w') as f:
            f.write(work_url)
    
    return data

def get_author_list(start_url):

    page_list = []
    item_list = []

    try:
        res = requests.get(start_url).text
    except ConnectionError:
        sleep(5)
        res = requests.get(start_url).text
    except:
        with open('./log','a+') as f :
            f.write('error = ' + start_url) 
    html = etree.HTML(res)
    #next_page = html.xpath('normalize-space(/html/body/div[2]/div[2]/ul/li[4]/a/@href)')
    next_page = html.xpath('normalize-space(//*[@rel="next"]/@href)')
    page_items = html.xpath('//*[@class="thumbnail"]')
    
    for i in page_items:
        item_url = i.xpath('normalize-space(@href)')
        item_name = i.xpath('normalize-space(div/text())')
        item_time = i.xpath('normalize-space(a/div[2]/text())')
        item_count = i.xpath('normalize-space(a/div[3]/text())')
        item_list = [item_name, item_url, item_time, item_count]
        page_list.append(item_list)

    return next_page, page_list

def save_csv(data):
    rows = [
        (str(data['title']),str(data['work_url']), str(data['author']), 
        str(data['author_url']), str(data['category']), str(data['img_url']), 
        str(data['upload_time']))
    ]

    with open('test.csv','a+')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)
        print('success')



def main():

    # start_url = 'http://www.cnu.cc/users/inspiration/158247'
    # start_url = 'http://www.cnu.cc/works/304897'
    start_url = 'http://www.cnu.cc/users/recommended/158247'

    # start_url = 'http://www.cnu.cc/users/861188'
    # start_url = 'http://www.cnu.cc/discoveryPage/hot-0'
    # start_url = 'http://www.cnu.cc/users/inspiration/158247?page=2'
    # start_url = 'http://www.cnu.cc/categories/%E4%BA%BA%E5%83%8F%E6%91%84%E5%BD%B1'
    # start_url = 'http://www.cnu.cc/discoveryPage/hot-%E6%97%85%E8%A1%8C'
    # start_url = 'http://www.cnu.cc/discoveryPage/hot-%E5%BB%BA%E7%AD%91'
    # start_url = 'http://www.cnu.cc/inspirationPage/recent-0'
    # start_url = 'http://www.cnu.cc/inspirationPage/recent-111'
    # start_url = 'http://www.cnu.cc/works/382214'
    # start_url = 'http://www.cnu.cc/works/304897'
    if start_url.split('/')[3] == 'works':
        item_url = start_url
        data = get_work_data(item_url)
        t = DownloadTask(data)
        t.start()
        # save_csv(data)
        # save_images(data)
    else:
        while start_url:
            start_url, page_list = get_author_list(start_url)
            # start_url = next_page

            for item in page_list:
                item_url = item[1]
                data = get_work_data(item_url)
                t = DownloadTask(data)
                t.start()




                

if __name__ == "__main__":
    
    main()