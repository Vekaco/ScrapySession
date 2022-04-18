# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class BasicCrawlPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('serial_number'):
            item['serial_number'] = item['serial_number'][0].zfill(3)
            return item
        else:
            raise DropItem(f"Missing serial_number")



