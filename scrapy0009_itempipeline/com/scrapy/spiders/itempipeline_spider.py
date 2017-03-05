import scrapy
from scrapy.loader import ItemLoader

from com.scrapy.articleitems import ArticleItems


class ItemPipelineSpider(scrapy.Spider):
    name = "itempipeline"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]
    def parse(self, response):
       author=ItemLoader(item=ArticleItems(),response=response) 
       for x in response.xpath("//div[@class='quote']"):
           author.add_css('text', '.text::text')
           author.add_css('author','.author::text')
           author.add_css('tags','.tag::text')
           author.add_value('last_updated', 'today')
       return author.load_item()
