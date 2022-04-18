import datetime
import socket

import scrapy
from urllib import parse
from basic_crawl.items import BasicCrawlItem
from lxml.builder import unicode
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join


class BasicSpiderSpider(scrapy.Spider):
    name = 'basic_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        """This function parses douban movie top250 list
        @url https://movie.douban.com/top250
        @returns items 25
        @scrapes serial_number movie_url movie_name introduce star evaluate quote
        @scrapes seed_url project spider server timestamp
        """
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for movie in movie_list:
            loader = ItemLoader(item=BasicCrawlItem(), selector=movie)
            loader.add_xpath('serial_number', './/div[@class="item"]//em/text()')
            loader.add_xpath('movie_url', './/div[@class="hd"]//a/@href')
            loader.add_xpath('movie_name', './/div[@class="info"]//div[@class="hd"]//span[@class="title"]/text()',
                             MapCompose(lambda i: "".join(i.split())))
            loader.add_xpath('introduce', './/div[@class="info"]//div[@class="bd"]/p[1]/text()',
                             MapCompose(lambda i: "".join(i.split())))
            loader.add_xpath('star', './/div[@class="star"]/span[@class="rating_num"]/text()', MapCompose(float))
            loader.add_xpath('evaluate', './/div[@class="star"]//span[4]/text()')
            loader.add_xpath('quote', './/p[@class="quote"]//span[@class="inq"]/text()')
            loader.add_value('seed_url', response.url)
            loader.add_value('project', self.settings.get('BOT_NAME'))
            loader.add_value('spider', self.name)
            loader.add_value('server', socket.gethostname())
            loader.add_value('timestamp', datetime.datetime.now().strftime('%c'))
            yield loader.load_item()
        next_link = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_link:
            next_link = next_link[0]
            yield Request(parse.urljoin(response.url, next_link))
        pass
