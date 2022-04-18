import scrapy
from scrapy.spiders import SitemapSpider
from datetime import datetime
from ssga.items import SsgaItem


class SitemapSpiderSpider(SitemapSpider):
    name = 'sitemap_spider'
    allowed_domains = ['yourdomain.com']
    sitemap_urls = ['https://yourdomain.com/robots.txt']
    sitemap_rules = [
        # parse page with parse_hk for those urls contains /hk/en
        ('/hk/en/', 'parse_hk'),
        ('/sg/en/', 'parse_sg'),
        #...
    ]

    # filter urls those modified later than 2015
    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime(entry['lastmod'], '%Y-%m-%d')
            if date_time.year >= 2015:
                yield entry

    # parsing data by rules
    def parse_hk(self, response):
        item = SsgaItem()
        item['title'] = response.xpath('//head//title/text()').extract()
        item['url'] = response.url
        yield item

    def parse_sg(self, response):
        item = SsgaItem()
        item['title'] = response.xpath('//head//title').extract()
        item['url'] = response.url
        yield item
