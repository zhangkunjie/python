import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders.feed import XMLFeedSpider


class SpiderDemo2(CrawlSpider):
    name = 'SpiderDemo2'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        #Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),
        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('/author/\w+', )), callback='parse_item'),
    )
    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        birthday=response.css(".author-born-date::text").extract_first()
        print(birthday)
        