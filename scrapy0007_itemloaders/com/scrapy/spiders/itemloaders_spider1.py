import scrapy
from scrapy.loader import ItemLoader
from com.scrapy.articleitems import ArticleItems
class ItemLoadersSpide1(scrapy.Spider):
    name = "itemloadersspider1"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/"
    ]
    def parse(self, response):
       for x in response.xpath("//div[@class='quote']"):
           author=ItemLoader(item=ArticleItems(),response=response)
           author.add_css('text', '.text::text')
           author.add_css('author','.author::text')
           author.add_css('tags','.tag::text')
           author.add_value('last_updated', 'today')
           author.load_item()
           """
           print(x.css(".text::text").extract())
           print(x.css(".author::text").extract())
           print(x.css(".tag::text").extract())
           #author.add_xpath('text','')
           """