import scrapy
from scrapy.loader import ItemLoader

from com.scrapy.articleitems import AuthorItems
from com.scrapy.productitem import Product


class ItemLoadersSpide2(scrapy.Spider):
    name = "itemloadersspider2"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/"
    ]
    def parse(self, response):
        il = ItemLoader(item=Product())
        il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
        il.add_value('price', [u'&euro;', u'<span>1000</span>'])
        il.load_item()
