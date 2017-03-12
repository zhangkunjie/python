from time import sleep
import time

import scrapy

from com.scrapy.items import JobInfoItems
class LagouSpider(scrapy.Spider):
    name = 'lagouspider'
    start_urls = ['https://www.lagou.com']
    def parse(self, response):
        for href in response.css("div.menu_sub dl dd a::attr('href')").extract():
            #详情页抓取
           #print(href) 
           for n in range(1,30) :
                job_list_url="https:"+href+str(n)+"/"
            #   print(job_list_url)
               #time.sleep(3) 
                yield scrapy.Request(job_list_url,
                                 callback=self.parse_jobs)
    def parse_jobs(self, response):
        print("AAAAAAAAAAAA"+response.url)
        jobInfoItems=[]
        for list_item_top in response.css("div.list_item_top"):
            jobInfoItems=JobInfoItems()
            jobInfoItems['j_id']=int(list_item_top.css(".position_link::attr(href)").extract_first().strip()[21:][:-5])
            jobInfoItems['url']=list_item_top.css(".position_link::attr(href)").extract_first().strip()[2:]
            jobInfoItems['name']=list_item_top.css(".position_link h2::text").extract_first().strip() 
            #工作类别
            jobInfoItems['category']=response.url.split("/")[-3]
            jobInfoItems['address']=list_item_top.css(".add em::text").extract_first().strip()
            jobInfoItems['c_id']=list_item_top.css("div.company_name a::attr(href)").extract_first().strip()[23:][:-5] 
            jobInfoItems['c_url']=list_item_top.css("div.company_name a::attr(href)").extract_first().strip()[2:] 
            jobInfoItems['c_name']=list_item_top.css("div.company_name a::text").extract_first().strip() 
            industry=list_item_top.css("div.industry::text").extract_first().strip()
            jobInfoItems['industry']=industry.split("/")[0].strip()
            jobInfoItems['financing_stage']=industry.split("/")[1].strip()
            jobInfoItems['money']=list_item_top.css(".money::text").extract_first().strip()
            experience=list_item_top.css(".li_b_l::text").extract()[2].strip()
            jobInfoItems['experience']=experience.split("/")[0]
            jobInfoItems['education']=experience.split("/")[1]
            yield jobInfoItems
