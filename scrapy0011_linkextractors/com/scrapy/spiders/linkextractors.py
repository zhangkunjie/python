from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spiders.crawl import Rule, CrawlSpider

"""
使用LinkExtractor从网页中获取链接，直接请求
注意：主类需要继承CrawlSpider
并且解析方法不能叫parse()
参数:    

    allow (a regular expression (or list of)) – a single regular expression (or list of regular expressions) that the (absolute) urls must match in order to be extracted. If not given (or empty), it will match all links.
    deny (a regular expression (or list of)) – a single regular expression (or list of regular expressions) that the (absolute) urls must match in order to be excluded (ie. not extracted). It has precedence over the allow parameter. If not given (or empty) it won’t exclude any links.
    allow_domains (str or list) – a single value or a list of string containing domains which will be considered for extracting the links
    deny_domains (str or list) – a single value or a list of strings containing domains which won’t be considered for extracting the links
    deny_extensions (list) – a single value or list of strings containing extensions that should be ignored when extracting links. If not given, it will default to the IGNORED_EXTENSIONS list defined in the scrapy.linkextractor module.
    restrict_xpaths (str or list) – is a XPath (or list of XPath’s) which defines regions inside the response where links should be extracted from. If given, only the text selected by those XPath will be scanned for links. See examples below.
    tags (str or list) – a tag or a list of tags to consider when extracting links. Defaults to ('a', 'area').
    attrs (list) – an attribute or list of attributes which should be considered when looking for links to extract (only for those tags specified in the tags parameter). Defaults to ('href',)
    canonicalize (boolean) – canonicalize each extracted url (using scrapy.utils.url.canonicalize_url). Defaults to True.
    unique (boolean) – whether duplicate filtering should be applied to extracted links.
    process_value (callable) – see process_value argument of BaseSgmlLinkExtractor class constructor
"""
class LinkExtractorsSpider(CrawlSpider):
    name = "LinkExtractorsSpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]
    rules={
        Rule(LinkExtractor(allow=('/tag/\w+', )), callback='parse_tags'),    
        Rule(LinkExtractor(allow=('/author/\w+', )), callback='parse_author'),
           }
    def parse_author(self, response):
        for author in response.css('.author-born-date::text').extract():
            print(author)         
    def parse_tags(self, response):
        for tag in response.css('.text::text').extract():
            print(tag)     