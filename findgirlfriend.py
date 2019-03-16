from wxpy import *
import requests
from threading import Timer

'''
作者：pk哥
公众号：Python知识圈
日期：2018/08/16
代码解析详见公众号「Python知识圈」。

'''


bot = Bot(cache_path=True)


def get_msg():
    url = 'http://open.iciba.com/dsapi/'   # 金山词霸每日一句 api 链接
    html = requests.get(url)
    content = html.json()['content']  # 获取每日一句英文语句
    note = html.json()['note']        # 获取每日一句英文的翻译语句
    return content, note


def send_msg():
    try:
        msgs = get_msg()
        content = msgs[0]
        note = msgs[1]
        my_friend = bot.friends().search(u'机器人')[0]  # 此处是对方自己的昵称，不是微信号，也不是你的备注。
        my_friend.send(content)  # 发送英文语句
        my_friend.send(note)     # 发送英文翻译
        my_friend.send(u'来自 brucepk 的问候')  # 自定义语句，根据自己情况更改
        t = Timer(86400, send_msg)  # Timer（定时器）是 Thread 的派生类，用于在指定时间后调用一个方法。
        t.start()
    except BaseException:
        my_friend = bot.friends().search(u'brucepk')[
            0]  # 发送不成功，则发送消息给自己，提醒消息发送失败
        my_friend.send(u'消息发送失败')


if __name__ == '__main__':
    send_msg()
