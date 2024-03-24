# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose, Compose

class BookparserItem(scrapy.Item):    # define the fields for your item here like:
    # name = scrapy.Field()

def process_author(value):
    value[0] = value[0].strip()
    return value

def process_fothos(value:str):
    print()
    if value.startswith('//'):
        value = 'https:' + value.split()[0]
    else:
        value = value.split()
    return value

class BookparserItem(scrapy.Item):
    author = scrapy.Field(input_processor=Compose(process_author), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(process_fothos())
    pass
