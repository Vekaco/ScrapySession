# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BasicCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()
    movie_url = scrapy.Field()
    movie_name = scrapy.Field()
    crew = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    evaluate = scrapy.Field()
    quote = scrapy.Field()
    seed_url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    timestamp = scrapy.Field()
    pass
