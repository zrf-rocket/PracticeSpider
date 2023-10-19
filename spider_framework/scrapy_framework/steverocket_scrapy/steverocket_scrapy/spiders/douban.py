import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse, Headers, JsonRequest

from steverocket_scrapy.items import DoubanItem
class DoubanSpider(scrapy.Spider):
    """
    spider核心  添加解析页面的代码
    """
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        # "https://movie.douban.com",
        'https://movie.douban.com/top250?start=0&filter='
    ]

    def parse(self, response: HtmlResponse):
        pass
