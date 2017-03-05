from scrapy.spiders.sitemap import SitemapSpider


class SpiderDemo5(SitemapSpider):
    """
    SitemapSpider使您爬取网站时可以通过 Sitemaps 来发现爬取的URL。
    其支持嵌套的sitemap，并能从 robots.txt 中获取sitemap的url。
    sitemap_urls
    包含您要爬取的url的sitemap的url列表(list)。 您也可以指定为一个 robots.txt ，spider会从中分析并提取url。
    sitemap_rules
    一个包含 (regex, callback) 元组的列表(list):
    regex 是一个用于匹配从sitemap提供的url的正则表达式。 regex 可以是一个字符串或者编译的正则对象(compiled regex object)。
    callback指定了匹配正则表达式的url的处理函数。 callback 可以是一个字符串(spider中方法的名字)或者是callable。
        例如:
        sitemap_rules = [('/product/', 'parse_product')]
        规则按顺序进行匹配，之后第一个匹配才会被应用。
        如果您忽略该属性，sitemap中发现的所有url将会被 parse 函数处理。
    sitemap_follow
        一个用于匹配要跟进的sitemap的正则表达式的列表(list)。其仅仅被应用在 使用 Sitemap index files 来指向其他sitemap文件的站点。
        默认情况下所有的sitemap都会被跟进。
    sitemap_alternate_links
        指定当一个 url 有可选的链接时，是否跟进。 有些非英文网站会在一个 url 块内提供其他语言的网站链接。
        例如:
        <url>
            <loc>http://example.com/</loc>
            <xhtml:link rel="alternate" hreflang="de" href="http://example.com/de"/>
        </url>
       当 sitemap_alternate_links 设置时，两个URL都会被获取。 当 sitemap_alternate_links 关闭时，只有 http://example.com/ 会被获取。
       默认 sitemap_alternate_links 关闭。
   """
    name = 'SpiderDemo5'
    sitemap_urls = ['http://www.apple.com/sitemap.xml']
    sitemap_rules = [
        ('/mac/', 'parse_mac'),
        ('/itunes/', 'parse_itunes'),
        ('', 'parse')
    ]
    def parse(self, response):
        self.log("default parsing method for {}".format(response.url))
    def parse_mac(self, response):
        self.log("parse_mac method for {}".format(response.url))
    def parse_itunes(self, response):
        self.log("parse_itunes method for {}".format(response.url))