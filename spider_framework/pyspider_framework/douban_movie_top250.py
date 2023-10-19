#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2023-10-19 19:08:58
# Project: douban_top250
# @author:SteveRocket
# @Date:2023/10/19
# @File:douban_movie_top250
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from pyspider.libs.base_handler import *


class DoubanSpider(BaseHandler):
    crawl_config = {
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://movie.douban.com/top250', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.item > .info > .hd > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "title": response.doc('h1 > span').text(),
            "rating": response.doc('.rating_num').text(),
            "director": response.doc('.attrs > a').eq(0).text(),
            "actors": [a.text() for a in response.doc('.actor > .info > a').items()],
        }
