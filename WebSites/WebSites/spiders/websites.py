''' 
  * @author   remonl
  * @coding    utf-8
'''
import scrapy
import urllib
import os
from ..items import WebsitesItem
from urllib.parse import urlparse

class WebsitesSpider(scrapy.Spider):
    # 爬虫名，启动爬虫时需要的参数 *必需
    name = 'websites'
    # 爬取域范围，允许爬虫在这个域名下爬取 可选
    allowed_domains = ['cn.bing.com']
    # allowed_domains = ['m.baidu.com']
    start_urls = list()
    class_path = os.path.expanduser('websites.txt')

    with open(class_path,'r',encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            # 爬虫执行后将从这个列表里获取网站名称进行爬取数据
            # start_urls.append('http://m.baidu.com/s?word=' + urllib.parse.quote(word))
            start_urls.append("http://cn.bing.com/search?&q=" + urllib.parse.quote(word))

    def parse(self, response):
        node_list = response.xpath('//div["b_content"]//ol[@id]/li[1]/div[@class="b_title"]')
        # node_list = response.xpath("./div[@class='result c-container new-pmd']")
        # node_list = response.xpath('div[@class="result c-container"]/h3/a')

        # current_page = response.xpath('div[@id="page"]/strong/span[@class="pc"]/text()').extract_first()
        # node_list = response.xpath('div[@class="result c-container"]/h3/a')

        for node in node_list:
            # 创建 item 字段对象，用来存储信息
            item = WebsitesItem()
            # extract 将 xpath 转换为 Unicode 字符串
            item['urls'] =str(response)
            item['name'] = node.xpath('./h2/a/strong/text()').extract()
            item['description'] = node.xpath('./h2/a/@href').extract()

            # url 转换成 域名
            # description = node.xpath('./h2/a/@href').extract()
            # item['description'] = urllib.parse.urlparse(description).netloc.lstrip('http://')
            # dns = urllib.parse.urlparse(item).netloc.lstrip('http://')

            # 返回提取到的 每个 item 数据，给管道文件处理，同时还会回来继续执行后面的代码
            yield item
