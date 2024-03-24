from scrapy.crawler import CrawlerProcess
import scrapy.utils.reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from bookparser.spiders.book24 import Book24Spider

if __name__== '__main__':
    configure_logging()
    scrapy.utils.reactor.install_reactor( 'twisted.internet.asyncioreactor.AsyncioSelectorReactor' )
    process = CrawlerProcess(get_project_settings())
    query = input()
    process.crawl(Book24Spider, query='детектив')
    process.start()

