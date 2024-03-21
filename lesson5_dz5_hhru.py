from os import name

import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


def responsexpath(param):
    pass


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = [
        "https://spb.hh.ru/search/vacancy?hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&text=&enable_snippets=false&L_save_area=true"]

    def parse(self, response: HtmlResponse):

        next_page = responsexpath("//a[@data-qa='pager-next']/@href").getall()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@target='_blank']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        nam = response.xpath("//h1/text()").get()
        salary = response.xpath("//span[@class='bloko-header-section-2']//text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url)

    print()
