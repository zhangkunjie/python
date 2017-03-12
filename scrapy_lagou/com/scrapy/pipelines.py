# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
def dbHandle():
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql',db='test',charset='utf8')
        return conn
class WriteToMysqlPipeline(object):
    def process_item(self, item, spider):
        dbObject =dbHandle()
        cursor = dbObject.cursor()
        sql = "insert into position (j_id,url,name,category,address,c_id,c_url,c_name,industry,financing_stage,money,experience,education) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(item['j_id'],item['url'],item['name'],item['category'],item['address'],item['c_id'],item['c_url'],item['c_name'],item['industry'],item['financing_stage'],item['money'],item['experience'],item['education']))
        dbObject.commit()
        return item   
