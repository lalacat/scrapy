from scrapy.spiders import Spider


class Spider3(Spider):
    name = "task3"
    custom_settings = ["URL = https://www.smzdm.com/homepage/json_more?p="]

    def __init__(self):
        super(Spider3,self).__init__()
        self.url = self.settings["URL"]

    def start_requests(self):
        start_url = list()

        for i in range(1):
            i = str(i)
            u = self.url + i
            start_url.append(u)

        for url in start_url:
            yield url

