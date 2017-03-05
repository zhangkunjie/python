import scrapy
class ArticleItems(scrapy.Item):
    text=scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    