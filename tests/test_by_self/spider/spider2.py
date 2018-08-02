from scrapy.spiders import Spider


class Spider2(Spider):
    name = "task2"
    custom_settings = ["URL = https://www.smzdm.com/homepage/json_more?p="]

    def __init__(self):
        super(Spider2,self).__init__()
        self.url = self.settings["URL"]

    def start_requests(self):
        start_url = list()

        for i in range(1):
            i = str(i)
            u = self.url + i
            start_url.append(u)

        for url in start_url:
            yield url

