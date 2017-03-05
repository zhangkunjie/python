# -*- coding: utf-8 -*-
import scrapy
class SelectorsDemo3(scrapy.Spider):
    #正则表达式选择器
    name = "SelectorsDemo3"
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    def parse(self, response):
        print(response.css('.author').re(r'A\s*(.*)'))