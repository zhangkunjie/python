# -*- coding: utf-8 -*-
import scrapy
class SelectorsDemo1(scrapy.Spider):
    #css和xpath选择器的比较
    name = "SelectorsDemo1"
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = [
        'http://quotes.toscrape.com/',
    ]
    def parse(self, response):
       print(response.xpath('//title/text()').extract())
       print(response.css('title::text').extract())
       
       print(response.xpath("//div[@class='quote']/span/a/@href").extract())
       print(response.css('.quote span>a::attr(href)').extract())
       
       
       print(response.xpath("//div[@class='tags']/a/@href").extract())
       print(response.css('.tags .tag::attr(href)').extract())
