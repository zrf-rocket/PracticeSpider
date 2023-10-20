# @author:SteveRocket 
# @Date:2023/10/20
# @File:demo1
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
import requests
import json

appid = ''
appsecret = ''

# 微信公众号API接口调用
def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid, appsecret)
    response = requests.get(url)
    access_token = response.json().get('access_token')
    if not access_token:
        access_token = json.loads(response.text)
    return access_token


access_token = get_access_token()
print(access_token)


def get_article_list():
    url = 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token={}'.format(access_token)
    data = {
        "type": "news",
        "offset": 0,
        "count": 20
    }
    response = requests.post(url, json=data)
    articles = response.json().get('item')
    article_list = []
    for article in articles:
        title = article.get('content').get('news_item')[0].get('title')
        url = article.get('content').get('news_item')[0].get('url')
        article_list.append({'title': title, 'url': url})
    return article_list


for item in get_article_list():
    print(item)


def get_freepublish_list():
    url = f"https://api.weixin.qq.com/cgi-bin/freepublish/batchget?access_token={access_token}"
    response = requests.post(url=url, json={
        "offset": 0,
        "count": 25,
        "no_content": 1
    })
    res = response.json()
    return res
