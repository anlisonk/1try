
import scrapy

class WeiboSpider(scrapy.Spider):
    name="weibo"
    start_urls=[
        "http://www.weibo.com/",
    ]
    def parse(self, respone):
        print(response.xpath('//div[@class="content"]').extract())