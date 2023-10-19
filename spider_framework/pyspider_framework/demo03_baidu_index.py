# @author:SteveRocket 
# @Date:2023/10/19
# @File:demo03_baidu_index
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from pyspider.libs.base_handler import *


class BaiDuSpider(BaseHandler):

    # 配置起始URL
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.baidu.com/', callback=self.index_page, validate_cert=False)

    # 抓取首页内容
    @config(priority=2)
    def index_page(self, response):
        return {
            "title": response.doc('title').text(),
            "url": response.url,
            "page": response.text,
        }

    # 对首页内容进行解析
    @config(age=10 * 24 * 60 * 60)
    def detail_page(self, response):
        return {
            "title": response.doc('title').text(),
            "url": response.url,
            "page": response.text,
        }