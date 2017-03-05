import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders.feed import XMLFeedSpider
class SpiderDemo1(XMLFeedSpider):
    """
    XMLFeedSpider被设计用于通过迭代各个节点来分析XML源(XML feed)。 迭代器可以从 iternodes ， xml ， html 选择。 鉴于 xml 以及 html 迭代器需要先读取所有DOM再分析而引起的性能问题， 一般还是推荐使用 iternodes 。 不过使用 html 作为迭代器能有效应对错误的XML。
    您必须定义下列类属性来设置迭代器以及标签名(tag name):
    iterator
        用于确定使用哪个迭代器的string。可选项有:
                'iternodes' - 一个高性能的基于正则表达式的迭代器
                'html' - 使用 Selector 的迭代器。 需要注意的是该迭代器使用DOM进行分析，其需要将所有的DOM载入内存， 当数据量大的时候会产生问题。
                'xml' - 使用 Selector 的迭代器。 需要注意的是该迭代器使用DOM进行分析，其需要将所有的DOM载入内存， 当数据量大的时候会产生问题。

        默认值为 iternodes 。
    itertag
        一个包含开始迭代的节点名的string。例如:
        itertag = 'product'
    namespaces
        一个由 (prefix, url) 元组(tuple)所组成的list。 其定义了在该文档中会被spider处理的可用的namespace。 prefix 及 uri 会被自动调用 register_namespace() 生成namespace。
        您可以通过在 itertag 属性中制定节点的namespace。
        例如:
        class YourSpider(XMLFeedSpider):
            namespaces = [('n', 'http://www.sitemaps.org/schemas/sitemap/0.9')]
            itertag = 'n:url'
            # ...
    除了这些新的属性之外，该spider也有以下可以覆盖(overrideable)的方法:
    adapt_response(response)
        该方法在spider分析response前被调用。您可以在response被分析之前使用该函数来修改内容(body)。 该方法接受一个response并返回一个response(可以相同也可以不同)。
    parse_node(response, selector)
        当节点符合提供的标签名时(itertag)该方法被调用。 接收到的response以及相应的 Selector 作为参数传递给该方法。 该方法返回一个 Item 对象或者 Request 对象 或者一个包含二者的可迭代对象(iterable)。
    process_results(response, results)
        当spider返回结果(item或request)时该方法被调用。 设定该方法的目的是在结果返回给框架核心(framework core)之前做最后的处理， 例如设定item的ID。其接受一个结果的列表(list of results)及对应的response。 其结果必须返回一个结果的列表(list of results)(包含Item或者Request对象)。
    """
    name = 'SpiderDemo3'
    start_urls = ['http://news.qq.com/newsgn/rss_newsgn.xml']
    iterator='iternodes'
    itertag='channel'
    def parse_node(self, response,node):
        print(node.xpath("title").extract_first())
        titles=node.xpath("item/title/text()").extract()
        for title in titles:
         print(title)
