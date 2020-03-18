from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from lxml import etree
import requests
import os


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 网页下滑等待时间
sleep_time = 1

# 要爬取的作品网页
url = 'http://www.cnu.cc/works/389493'
# CNU.CC反爬混淆图片地址
hide_url = 'http://imgoss.cnu.cc/assets/images/1_1.gif'
#def js(n):
#   return 'window.scrollTo(0,{})'.format(n)

def get_res(url):
    """获取完整网页"""

    # 无头浏览器
    driver = webdriver.Chrome(options=chrome_options) 
    # 真实浏览器
    #driver = webdriver.Chrome() 
    #获取网页主页面
    driver.get(url)
    # 获取网页高度
    clientHeight = driver.execute_script('return document.body.clientHeight')
    # 页面下滑 1000
    page_down = 'window.scrollBy(0,1000)'
    page_up = 'window.scrollBy(0,-1000)'

    height = 0
    STR_READY_STATE = ''
    while height < clientHeight:
        driver.execute_script(page_down)
        STR_READY_STATE = ''
        #print(driver.execute_script('window.onload'))
        height += 1000
        print(height)
        #print(height, clientHeight)
        sleep(sleep_time)
        STR_READY_STATE = driver.execute_script('return document.readyState')
        print(STR_READY_STATE)
        if STR_READY_STATE == 'interactive':
            #driver.execute_script(page_up)
            height = 0
            sleep(sleep_time)

    return driver.page_source
            
    

def get_content_bs(source):
    data = {}
    img_url = []
    soups = BeautifulSoup(source, 'lxml')
    author = soups.find('strong').get_text("", strip=True)
    title = soups.find('h2').get_text("", strip=True)
    count = soups.find('span', class_="read").string
    author_url = soups.find('span', class_="author-info").a.get("href")
    for name in soups.body.select('span[data-original-title]'):
        upload_time = name.attrs['data-original-title']
        if upload_time:
            break 
    for img in soups.body.select('img[data-original]'):
        imgurl = img.attrs['src']
        img_url.append(imgurl)


        # # 判断是否获取到真实连接
        # if img_url == hide_url:
        #     global sleep_time
        #     sleep_time += 0.5
        #     get_content_bs(url)
    data['author'] = author
    data['title'] = title
    data['author_url'] = author_url
    data['upload_time'] = upload_time
    data['count'] = count
    data['img_url'] = img_url

    return data


def get_content_xpath(source):
    data = {}
    #print(source)
    html = etree.HTML(source)
    img_url = html.xpath('//*[@id="work_body"]/div/img/@src')
    title = html.xpath('normalize-space(/html/body/div[1]/div[2]/h2/text())')
    author = html.xpath('normalize-space(/html/body/div[1]/div[2]/span/a/strong/text())')
    upload_time = html.xpath('/html/body/div[1]/div[2]/span/span/@data-original-title')
    author_url = (html.xpath('normalize-space(/html/body/div[1]/div[2]/span/a/@href)'))
    count = html.xpath('normalize-space(/html/body/div[1]/div[2]/div/span[2]/span/text())')

    data['author'] = author
    data['title'] = title
    data['author_url'] = author_url
    data['upload_time'] = upload_time
    data['count'] = count
    data['img_url'] = img_url

    return data


def save_images(data):
    path = data['title']
    # if not os.path.exists('./'+path):
    #     os.mkdir(path)

    for i in data['img_url']:
        print(i)
        # image = requests.get(i)
        # name = i.split('?')[0].split('/')[-1]
        # with open('./'+path+'/'+name, 'wb') as f:
        #     f.write((image.content))
        #     print('save complete:{}'.format(name))
        #     f.close()



def get_author_list(url):
    page_list = []
    item_list = []
    res = requests.get(url).text
    html = etree.HTML(res) 
    #print(type(html))
    page_items = html.xpath('//*[@id="recommendForm"]/div')
    for i in page_items:
        item_url = i.xpath('normalize-space(a/@href)')
        item_name = i.xpath('normalize-space(a/div/text())')
        item_time = i.xpath('normalize-space(a/div[2]/text())')
        item_count = i.xpath('normalize-space(a/div[3]/text())')
        item_list = [item_name, item_url, item_time, item_count]
        page_list.append(item_list)
        data = get_content_xpath(item_url)
    
    return page_list


    #print(page_list)
    
if __name__ == '__main__':
    # source = get_res(url)
    # data = get_content_xpath(source)
    # print(data)
    #save_images(data)
    page_list = get_author_list('http://www.cnu.cc/users/133229')

    for i in page_list:
        source = get_res(i[1])
        data = get_content_xpath(source)
        for j in data['img_url']:
            if j == hide_url:
                print(data['title'])
                print(j)
                break
        save_images(data)

            