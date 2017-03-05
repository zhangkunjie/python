import scrapy
from com.scrapy.items import MyItem
class QuotesSpider(scrapy.Spider):
    """
    使用formdata来进行登陆操作
    """
    name = "requestandresponsedemo2"
    start_urls = [
        "https://www.douban.com/accounts/login"
    ]
    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'form_email': '907535517@qq.com', 'password': 'PPxy198861'},
            callback=self.after_login
        )
    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
        else:
            print(response.body)
            
            return