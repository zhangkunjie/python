# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JobInfoItems(scrapy.Item):
    # define the fields for your item here like:
    j_id=scrapy.Field()
    url= scrapy.Field()
    name= scrapy.Field()
    category=scrapy.Field()
    address= scrapy.Field()
    c_id=scrapy.Field()
    c_url= scrapy.Field()
    c_name= scrapy.Field()
    industry= scrapy.Field()
    financing_stage= scrapy.Field()
    money= scrapy.Field()
    experience= scrapy.Field()
    education= scrapy.Field()
    pass
