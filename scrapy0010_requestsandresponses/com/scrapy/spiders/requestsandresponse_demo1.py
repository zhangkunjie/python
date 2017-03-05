"""
class scrapy.http.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])
cookie的两种用法：
    Using a dict:
    request_with_cookies = Request(url="http://www.example.com",
                                   cookies={'currency': 'USD', 'country': 'UY'})
    Using a list of dicts:
    request_with_cookies = Request(url="http://www.example.com",
                                   cookies=[{'name': 'currency',
                                            'value': 'USD',
                                            'domain': 'example.com',
                                            'path': '/currency'}])
class scrapy.http.Response(url[, status=200, headers=None, body=b'', flags=None, request=None])
A Response object represents an HTTP response, which is usually downloaded (by the Downloader) and fed to the Spiders for processing.
Parameters:    
url (string) – the URL of this response
status (integer) – the HTTP status of the response. Defaults to 200.
headers (dict) – the headers of this response. The dict values can be strings (for single valued headers) or lists (for multi-valued headers).
body (str) – the response body. It must be str, not unicode, unless you’re using a encoding-aware Response subclass, such as TextResponse.
flags (list) – is a list containing the initial values for the Response.flags attribute. If given, the list will be shallow copied.
request (Request object) – the initial value of the Response.request attribute. This represents the Request that generated this response.
"""
import scrapy
from com.scrapy.items import MyItem
class QuotesSpider(scrapy.Spider):
    name = "requestandresponsedemo1"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]
    def parse(self, response):
        item = MyItem()
        item['main_url'] = response.url
        request = scrapy.Request("http://quotes.toscrape.com/",
                                 callback=self.parse_page2)
        """通过meta传递参数"""
        request.meta['item'] = item
        yield request
    def parse_page2(self, response):
        item = response.meta['item']
        item['other_url'] = response.url
        yield item