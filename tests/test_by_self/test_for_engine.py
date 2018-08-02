from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

s = Settings()

cp = CrawlerProcess()
for name, module in cp.spider_loder._spiders.items():
    print(module)
    cp.crawl(module)
