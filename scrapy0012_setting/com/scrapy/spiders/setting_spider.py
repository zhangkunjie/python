import scrapy
class LoggingSpider(scrapy.Spider):
    name = "setting"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/"
    ]
 #获取系统设置   
    def parse(self, response):
        for key in self.settings.attributes.keys():
            print(key)
