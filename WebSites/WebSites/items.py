''' 
  * @author   remonl
  * @coding    utf-8
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebsitesItem(scrapy.Item):
    # define the fields for your item here like:
    urls = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
