#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2023-10-19 18:46:26
# Project: spider01
# @author:SteveRocket
# @Date:2023/10/19
# @File:demo01
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://hz.lianjia.com/ershoufang/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://hz.lianjia.com/ershoufang/', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.title').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        yield {
            'unit_price': response.doc('.unitPrice').text(),
            'title': response.doc('.main').text(),
            'sell_point': response.doc('.baseattribute > .content').text()
        }
