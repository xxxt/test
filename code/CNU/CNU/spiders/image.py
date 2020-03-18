# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from CNU.items import CnuItem

import re


class ImageSpider(CrawlSpider):
    name = 'image'
    allowed_domains = ['cnu.cc']
    start_urls = ['http://www.cnu.cc/discoveryPage/hot-0']

    rules = (
        Rule(LinkExtractor(allow=(r'http://www.cnu.cc/discoveryPage+.*'))), 
        Rule(LinkExtractor(allow=(r'http://www.cnu.cc/works/\d+')), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = CnuItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['name'] = sel.xpath('/html/body/div[1]/div[2]/h2/text()').extract()
        item['time'] = sel.xpath('/html/body/div[1]/div[2]/span/span/text()').extract()
        item['author'] = sel.xpath('/html/body/div[1]/div[2]/span/a/strong/text()').extract()
        item['author_url'] = sel.xpath('normalize-space(/html/body/div[1]/div[2]/span/a/@href)').extract()
        item['url'] = sel.xpath('normalize-space(//*[@id="imgs_json"])').re('(?<=img":")\d+/\d+/\w+.jpg')#.extract()

        return item
