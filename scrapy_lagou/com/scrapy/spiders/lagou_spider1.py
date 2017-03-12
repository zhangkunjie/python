from time import sleep
import time
import scrapy
from scrapy.loader import ItemLoader

from com.scrapy.items import JobInfoItems
class LagouSpider(scrapy.Spider):
    name = 'lagouspider1'
    start_urls = ['https://www.lagou.com/zhaopin/jinrong3fengkong/19/']
    def parse(self, response):
        for n in range(20,23) :
                job_list_url="https://www.lagou.com/zhaopin/jinrong3fengkong/"+str(n)+"/"
                yield scrapy.Request(job_list_url,
                                 callback=self.parse_jobs)
    def parse_jobs(self, response):
        print("AAAAAAA"+response.url)