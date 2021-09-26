import scrapy
from scrapy.http import HtmlResponse
import pymongo

client = pymongo.MongoClient("mongodb+srv://NaGul:<15s9pu03>@cluster0.qbjcy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.books


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/best/sale/']
    books_list_labirint = []

    def parse(self, response1:HtmlResponse):
        book_links_labirint = response1.xpath("//a[@class = 'product-title-link']/@href").extract()

        for links_books in book_links_labirint:
            yield response1.follow(links_books, callback=self.books_labirint_parse)
        print()
        pass

    def books_labirint_parse(self, response1:HtmlResponse):
        book_labirint = {'title': response1.xpath("//h1/text()").extract_first(),
                         'author': response1.xpath("//div[@class = 'authors']/a/text()").extract_first(),
                         'price': response1.xpath("//span[@class = 'buying-priceold-val-number']/text()").extract_first(),
                         'rating': response1.xpath("//div[@class = 'left']/div/text()").extract_first()
                         }

        db.insert_many(book_labirint)

        return book_labirint
        print()


