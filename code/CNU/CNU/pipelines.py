# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
setting = get_project_settings()


class CnuPipeline(object):

    def __init__(self):
        super().__init__()
        connection = pymongo.MongoClient(setting['MONGODB_SERVER'], setting['MONGODB_PORT'])
        db = connection[setting['MONGODB_DB']]
        self.collection = db[setting['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {} of blogpost from {}".format(data, item['url']))
        if valid:
            new_image = [{
                "name":item['name'],
                "time":item['time'],
                "author":item['author'],
                "url":item['url'],
                "author_url":item['author_url']
            }]
            self.collection.insert(new_image)



        return item
