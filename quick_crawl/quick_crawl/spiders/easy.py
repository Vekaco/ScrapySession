import datetime

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule
from quick_crawl.items import QuickCrawlItem


class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['movie.douban.com']#['www.gumtree.com']
    start_urls = ['https://movie.douban.com/top250']#['http://www.gumtree.com/flats-houses/london']

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]')),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="hd"]'), callback='parse_item')
    )

    def parse_item(self, response):
        #item = {}
        #item['title'] = response.xpath('//h1/text()').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        #item = QuickCrawlItem()
        #item['movie_url'] = response.url
        l = ItemLoader(item=QuickCrawlItem(), response=response)
        l.add_value('movie_url', response.url)
        l.add_xpath('movie_name', '//h1/span[1]/text()')
        l.add_xpath('year', '//h1//span[@class="year"]/text()',
                    MapCompose(lambda i: i.replace('(', ''),
                               lambda i: i.replace(')', '')))
        l.add_xpath('director', '//div[@id="info"]//span//span[@class="attrs"]//a[@rel="v:directedBy"]/text()')
        l.add_xpath('writer', '//div[@id="info"]//span//span[@class="attrs"]//a[not(@rel)]/text()',
                    MapCompose(lambda i: i.replace('更多...', '')))
        l.add_xpath('actors', '//div[@id="info"]//span//span[@class="attrs"]//a[@rel="v:starring"]/text()')
        l.add_xpath('category', '//div[@id="info"]//span[@property="v:genre"]/text()')
        l.add_xpath('country_region', '//div[@id="info"]//span[text()="制片国家/地区:"]/following-sibling::text()[1]')
        l.add_xpath('language', '//div[@id="info"]//span[text()="语言:"]/following-sibling::text()[1]')
        l.add_xpath('release_date', '//div[@id="info"]//span[@property="v:initialReleaseDate"]/text()')
        l.add_xpath('length', '//div[@id="info"]//span[@property="v:runtime"]/text()')
        l.add_xpath('alias', '//div[@id="info"]//span[text()="又名:"]/following-sibling::text()[1]')
        l.add_xpath('imdb', '//div[@id="info"]//span[text()="IMDb:"]/following-sibling::text()[1]')
        l.add_xpath('official_site', '//div[@id="info"]//span[text()="官方小站:"]/following-sibling::a/@href')
        l.add_xpath('introduce', '//div[@class="indent"]//span[contains(@class, "all")]/text()',
                    MapCompose(lambda i: "".join(i.split())))
        l.add_xpath('star', '//strong[contains(@class, "rating_num")]/text()')
        l.add_value('timestamp', datetime.datetime.now().strftime('%c'))
        return l.load_item()
