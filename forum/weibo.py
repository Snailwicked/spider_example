from headers import random_headers as headers
import time,re
from dateutil.parser import parse as date_parser


def removehtml(html):
    p = re.compile('<[^>]+>')
    return p.sub("", html)


def get_comments(params):
    response = requests.get('https://m.weibo.cn/comments/hotflow', headers=headers, params=params)
    results = json.loads(response.text)
    if results["ok"] == 1:
        print("---------------评论数据----------------")
        for item in results["data"]["data"]:
            comment_publish_time = int(time.mktime(date_parser(str(item["created_at"])).timetuple()) * 1000)
            print("评论发布时间：",comment_publish_time,"*********","评论发布作者：",item["user"]["screen_name"])
            print("评论内容：",removehtml(item["text"]))
        if results["data"]["max_id"]:
            print("获取第二页评论数据需登录")
            # new_parms = list(params)
            # new_parms.append(("max_id", "{}".format(results["data"]["max_id"])))
            # get_comments(tuple(new_parms))
    else:
        print("---------------没有评论数据------------")


import json
if __name__ == '__main__':
    import requests
    for page in range(2,20):
        print(page)
        params = (
            ('containerid', '100103type=1&q=%E4%B8%AD%E5%85%B4'),
            ('page_type', 'searchall'),
            ('page', '{}'.format(page)),
        )
        response = requests.get('https://m.weibo.cn/api/container/getIndex', headers=headers, params=params)
        results = json.loads(response.text)
        if results["ok"] == 1:
            info_list_temp = results["data"]["cards"]

            for item in info_list_temp:
                print("----------------------"*20)
                isPass = 2
                source = "新浪微博-重点网站"
                content_info ={}
                publish_time = item["itemid"].split("&")[-2].split("=")[-1]
                print("发布时间：",publish_time)
                print("文本内容：",removehtml(item["mblog"]["text"]))
                account_id = item["mblog"]["user"]["id"]  # 账号id
                news_id = item["mblog"]["mid"]  # 账号id
                # print("账号id：",account_id)
                account_nickname = item["mblog"]["user"]["screen_name"]  # 个人账号昵称
                print("账号昵称：",account_nickname)
                account_url = item["mblog"]["user"]["profile_url"]  # 个人账号主页地址
                print("主页地址：",account_url)

                description = item["mblog"]["user"]["description"].strip()  # 个人简介
                print("个人简介：",description)
                params = (
                    ('id', '{}'.format(account_id)),
                    ('mid', '{}'.format(news_id)),
                    ('max_id_type', '0'),
                )
                get_comments(params)


