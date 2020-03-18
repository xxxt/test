# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanPipeline(object):
#     def process_item(self, item, spider):
#         return item


import pymongo

from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
# from scrapy import log


class DoubanPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        #Remove invalid data
        valid = True
        for data in item:
          if not data:
            valid = False
            raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
        if valid:
        #Insert data into database
            new_moive=[{
                "name":item['name'][0],
                "year":item['year'][0],
                "score":item['score'],
                "director":item['director'],
                "classification":item['classification'],
                "actor":item['actor']
            }]
            self.collection.insert(new_moive)
            # log.msg("Item wrote to MongoDB database %s/%s" %
            # (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
            # level=log.DEBUG, spider=spider) 
        return item