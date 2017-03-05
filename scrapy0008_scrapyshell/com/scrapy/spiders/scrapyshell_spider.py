import scrapy
class  ScrapyShellSpider(scrapy.Spider):
    name = "scrapyshell"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com"
    ]
    def parse(self, response):
        if ".com" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)