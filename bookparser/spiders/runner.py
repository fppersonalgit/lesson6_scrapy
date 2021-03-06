from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from bookparser import settings
from bookparser.spiders.book24 import Book24Spider
from bookparser.spiders.labirint import LabirintSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(Book24Spider)

    process.crawl(LabirintSpider)

    process.start()
