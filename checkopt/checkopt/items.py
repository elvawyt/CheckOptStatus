# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CheckoptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # timestamp = datetime.datetime.now()
   
    status_headline = scrapy.Field()
    links = scrapy.Field()
