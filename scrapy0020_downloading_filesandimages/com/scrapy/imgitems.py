# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ImageItems(scrapy.Item):
    image_urls = scrapy.Field()
    images=scrapy.Field()
