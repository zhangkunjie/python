import scrapy
from scrapy.loader import ItemLoader
from com.scrapy.imgitems import ImageItems

class  ImageDownloaderSpider(scrapy.Spider):
    name = "imagedownloader"
    start_urls = [
        "https://www.lagou.com/"
    ]
    def parse(self, response):
        img=ItemLoader(item=ImageItems(),response=response) 
        img_urls=response.css(".banner_bg img::attr(src)").extract()
        for img_url  in img_urls:
            print(img_url)
            img.add_value('image_urls', img_url)
        return img.load_item()
