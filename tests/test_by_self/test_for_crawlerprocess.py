from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

module = 'tests.test_by_self.spider'
          #'tests.test_by_self.spider.spider2',
          #'tests.test_by_self.spider.spider3'

settings = Settings({'SPIDER_MODULES': [module]})
cp = CrawlerProcess(settings)

for name, module in cp.spider_loader._spiders.items():
    print(module)
    cp.crawl(module)
cp.start()