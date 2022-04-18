# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LoginCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_url = scrapy.Field()
    movie_name = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    actors = scrapy.Field()
    category = scrapy.Field()
    country_region = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    length = scrapy.Field()
    alias = scrapy.Field()
    imdb = scrapy.Field()
    official_site = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    timestamp = scrapy.Field()
    pass
