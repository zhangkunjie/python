# -*- coding: utf-8 -*-
import scrapy
class SelectorsDemo2(scrapy.Spider):
    #嵌套选择器
    name = "SelectorsDemo2"
    allowed_domains = ['lagou.com/']
    start_urls = [
        'https://www.lagou.com/',
    ]
    def parse(self, response):
       job_class=response.xpath("//div[@class='menu_sub dn']/dl/dd/a")
       for job in job_class:
           print(job.xpath("text()").extract_first()+job.xpath("@href").extract_first())
