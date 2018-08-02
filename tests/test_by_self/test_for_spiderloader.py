
from scrapy.spiderloader import SpiderLoader
from scrapy.settings import Settings


module = 'tests.test_by_self.spider'
          #'tests.test_by_self.spider.spider2',
          #'tests.test_by_self.spider.spider3'

settings = Settings({'SPIDER_MODULES': [module]})
spider_loader = SpiderLoader.from_settings(settings)
for name, module in spider_loader._spiders.items():
    print(name,module)
