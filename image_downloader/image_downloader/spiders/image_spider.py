import urllib.parse

import scrapy
from scrapy.loader import ItemLoader
from image_downloader.items import ImageDownloaderItem


class ImageSpiderSpider(scrapy.Spider):
    name = 'image_spider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        loader = ItemLoader(item=ImageDownloaderItem(), response=response)

        loader.add_xpath('image_urls', '//p[@class="post-item-summary"]/a/img/@src')

        yield loader.load_item()
