import scrapy
from scrapy.http import HtmlResponse
import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://NaGul:<15s9pu03>@cluster0.qbjcy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.books


class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/knigi-bestsellery/']
    book_list = []

    def parse(self, response: HtmlResponse):
        book_links = response.xpath("//div[@class = 'product-card__content']/a/@href").extract()


        for link in book_links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response=HtmlResponse):
        book = {'title': response.xpath('//h1/text()').extract_first().replace('\n','').strip(),
                'author': response.xpath("//div[@class = 'product-characteristic__value']/a/text()").extract_first().replace('\n','').strip(),
                'price': response.xpath("//span[@class = 'app-price product-sidebar-price__price']/text()").extract_first().replace('\n','').strip(),
                'rating': response.xpath("//span[@class = 'rating-widget__main-text']/text()").extract_first().replace('\n','').strip()}
        print()
        self.book_list.append(book)
        db.insert_many(book)
        return book
