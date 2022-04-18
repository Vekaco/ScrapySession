# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from douban.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline:
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        table = mongo_db_collection

        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        #mydb.authenticate('username', 'password')
        self.post = mydb[table]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
