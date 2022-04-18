# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class SsgaPipeline:
    def __init__(self):
        self.file = None

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict() + "\n")
        self.file.write(line)
        print(item)
        return item

    def open_spider(self, spider):
        self.file = open('./ssga.jl', 'w')
        pass

    def close_spider(self, spider):
        self.file.close()
        pass
