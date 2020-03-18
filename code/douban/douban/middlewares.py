# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

import random  
from scrapy import signals  
from douban.settings import IPPOOL  

class MyproxiesSpiderMiddleware(object):  

      def __init__(self,ip=''):  
          self.ip=ip  

      def process_request(self, request, spider):  
          thisip=random.choice(IPPOOL)  
          print("this is ip:"+thisip["ipaddr"])
          request.meta["proxy"]="https://"+thisip["ipaddr"]  



# import logging,requests
# from scrapy.utils.project import get_project_settings
# settings = get_project_settings()
# from fake_useragent import UserAgent

# class RandomUserAgentMiddleware(object):
#     logger = logging.getLogger(__name__)
#     def __init__(self, crawler):
#         super(RandomUserAgentMiddleware, self).__init__()

#         self.ua = UserAgent()
#         self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')


#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler)

#     def process_request(self, request, spider):
#         def get_ua():
#             return getattr(self.ua, self.ua_type)
#         request.headers.setdefault('User-Agent', get_ua())
#         request.meta['proxy'] = 'http://' + self.proxy()

#     def proxy(self):
#         proxy = requests.get("http://127.0.0.1:5010/get").text
#         try:
#             print('get proxy ...')
#             # proxy = requests.get("http://127.0.0.1:5010/get").text
#             ip = {"http": "http://" + proxy, "https": "https://" + proxy}
#             r = requests.get("http://www.baidu.com", proxies=ip, timeout=4)
#             print(r.status_code)
#             if r.status_code == 200:
#                 return proxy
#         except:
#             print('get proxy again ...')
#             self.delete_proxy(proxy)
#             return self.proxy()

#     def process_response(self, request, response, spider):
#         '''对返回的response处理'''
#         # 如果返回的response状态不是200，重新生成当前request对象
#         if response.status != 200:
#             print("again response ip:")
#             # 对当前reque加上代理
#             request.meta['proxy'] = 'https://' + self.proxy()
#             return request
#         return response

#     def process_exception(self, request, exception, spider):
#         self.logger.debug('Get exception')
#         request.meta['proxy'] = 'https://' + self.proxy()
#         return request

#     def delete_proxy(self, proxy):
#         requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))