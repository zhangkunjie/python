# -*- coding: utf-8 -*-
from scrapy import Selector


class SelectorsDemo5():
   sel1 = Selector(text='<a href="#">Click here to go to the <strong>Next Page</strong></a>')
   print(sel1.xpath('//a//text()').extract())
   print(sel1.xpath("string(//a[1]//text())").extract())
   print(sel1.xpath("//a[1]").extract())
   print(sel1.xpath("string(//a[1])").extract())
   print(sel1.xpath("//a[contains(.//text(), 'Next Page')]").extract())
   print(sel1.xpath("//a[contains(., 'Next Page')]").extract())
   sel2 = Selector(text=" <ul class='list'><li>1a</li><li>2a</li><li>3a</li> </ul><ul class='list'><li>4a</li><li>5a</li><li>6a</li></ul>")
   print(sel2.xpath("//li[1]").extract())    
   print(sel2.xpath("(//li)[1]").extract())
   print(sel2.xpath("//ul/li[1]").extract())  
   print(sel2.xpath("(//ul/li)[1]").extract())  
   sel3 = Selector(text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>')
   print(sel3.css('.shout').xpath('./time/@datetime').extract())
   """
   文档：
   
xpath(query)
   寻找可以匹配xpath query 的节点，并返回 SelectorList 的一个实例结果，单一化其所有元素。列表元素也实现了 Selector 的接口。
   query 是包含XPATH查询请求的字符串。
   注解
   为了方便起见，该方法也可以通过 response.xpath() 调用

css(query)
   应用给定的CSS选择器，返回 SelectorList 的一个实例。
   query 是一个包含CSS选择器的字符串。
   在后台，通过 cssselect 库和运行 .xpath() 方法，CSS查询会被转换为XPath查询。
   注解
   为了方便起见，该方法也可以通过 response.css() 调用

extract()
   串行化并将匹配到的节点返回一个unicode字符串列表。 结尾是编码内容的百分比。

re(regex)
   应用给定的regex，并返回匹配到的unicode字符串列表。、
   regex 可以是一个已编译的正则表达式，也可以是一个将被 re.compile(regex) 编译为正则表达式的字符串。

register_namespace(prefix, uri)
   注册给定的命名空间，其将在 Selector 中使用。 不注册命名空间，你将无法从非标准命名空间中选择或提取数据。参见下面的例子。

remove_namespaces()
   移除所有的命名空间，允许使用少量的命名空间xpaths遍历文档。参加下面的例子。

__nonzero__()
   如果选择了任意的真实文档，将返回 True ，否则返回 False 。 也就是说， Selector 的布尔值是通过它选择的内容确定的。
  """   
  