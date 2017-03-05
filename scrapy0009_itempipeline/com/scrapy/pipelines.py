# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
当Item在Spider中被收集之后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理。
每个item pipeline组件(有时称之为“Item Pipeline”)是实现了简单方法的Python类。他们接收到Item并通过它执行一些行为，同时也决定此Item是否继续通过pipeline，或是被丢弃而不再进行处理。
以下是item pipeline的一些典型应用：
    清理HTML数据
    验证爬取的数据(检查item包含某些字段)
    查重(并丢弃)
    将爬取结果保存到数据库中
主要方法：
rocess_item(item, spider)

    每个item pipeline组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象， 或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。
    参数:    
        item (Item 对象) – 被爬取的item
        spider (Spider 对象) – 爬取该item的spider

此外,他们也可以实现以下方法:
open_spider(spider)
    当spider被开启时，这个方法被调用。
    参数:    spider (Spider 对象) – 被开启的spider
close_spider(spider)
    当spider被关闭时，这个方法被调用
import pymongo
import pymongo
import pymongo
    参数:    spider (Spider 对象) – 被关闭的spider    
import json
import json
import json
import pymysql
import pymysql
from cmath import e
import pymysql
from pymysql.err import e
import pymysql
from pymysql.err import e
from pymysql.err import e
主要用途：将数据插入到数据库
"""
import codecs
import json
import pymongo
import pymysql
import traceback

#将文件保存到json
class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open('/Users/user/Desktop/scrapy/author.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
#将数据保存到mysql
def dbHandle():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql', db='test')
    return conn
class MySQLStoreArticlePipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into article(text,author,tags,last_update) values (%s,%s,%s,%s)'
        print("AAAAAAAAAAAAAAAAAA"+item['author'][0])
        print("AAAAAAAAAAAAAAAAAA"+item['text'][0])
        print("AAAAAAAAAAAAAAAAAA"+item['tags'][0])
        try:
            cursor.execute(sql,(item['text'],item['author'],item['tags'],item['last_updated']))
            cursor.execute(sql,(item['author'][0],'B','C','D'))
            dbObject.commit()
        except  Exception:
            print("BBBBBBB")
            dbObject.rollback()
        return item   
        """    
#将数据保存到Mongo
"""   
class MongoPipeline(object):
    collection_name = 'scrapy_items'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def close_spider(self, spider):
        self.client.close()
    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
