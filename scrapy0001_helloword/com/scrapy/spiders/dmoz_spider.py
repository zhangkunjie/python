import scrapy

from com.scrapy import DmozItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://quotes.toscrape.com/tag/humor/page/1/"
    ]
    def parse(self, response):
        print("demo1:这个函数会获取从DmozSpider中回调回来的一些信息，比如URL")
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            print("获取的文件名字是："+filename)
            f.write(response.body)
        print("提取Item，使用selector选择器demo2:xpath/text()/extarct()/re的区别")
        """  
        /html/head/title: 选择HTML文档中 <head> 标签内的 <title> 元素
        /html/head/title/text(): 选择上面提到的 <title> 元素的文字
        //td: 选择所有的 <td> 元素
        //div[@class="mine"]: 选择所有具有 class="mine" 属性的 div 元素
        """ 
        print(response.xpath('//title'))  
        print( response.xpath('//title').extract())
        print(response.xpath('//title/text()'))
        print(response.xpath('//title/text()').extract())
        print(response.xpath('//title/text()').re('(\w+):'))
        print("demo3:xpath的嵌套调用")
        for sel in response.xpath("//div[@class='title-and-desc']"):
            #print(sel.extract())
            item = DmozItem()
            item['title'] =sel.xpath("a/div[@class='site-title']/text()").extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath("div[@class='site-descr ']/text()").extract()
            yield(item)
        print("demo4:数据保存到文件")
        #f=open("/Users/user/Desktop/spider_result")
    
        
        
