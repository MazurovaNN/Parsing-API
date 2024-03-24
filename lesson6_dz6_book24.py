import scrapy
from scrapy.http import HtmlResponse
import bookparser.items
from bookparser.items import BookparserItem
import scrapy.loader
from scrapy.loader import ItemLoader


class Book24Spider(scrapy.Spider):
    name = "book24"
    allowed_domains = ["book24.ru"]

    def __init__(self, **kwargs):
        super ().__init__(**kwargs)
        self.start_urls = [f"https://book24.ru/search/?q={kwargs.get ( 'query' )}"]

    def parse(self, response:HtmlResponse):
        links = response.xpath("//a[@class='product-card__name']/@href").get()
        for link in links:
            yield response.follow(callback=self.parse_book)

    def parse_book(self, response:HtmlResponse):
        # author = response.xpath("//a[@class='author-list__item smartLink']")
        # url = response.url
        # photos = response.xpath("//img[@class='product-poster__main-image']").getall()
        #
        # yield(Bookparser(author=author, url=url, photos=photos))
    loader = ItemLoader(Item=BookparserItem(), response = response)
    loader.add_xpath('author', "//a[@class='author-list__item smartLink']")
    loader.add_xpath('url', response.url)
    loader.add_xpath('photos', "//img[@class='product-poster__main-image']")

    yield loader._local_item()
