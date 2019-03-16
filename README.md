# Python 教你脱单，定时给对象发早安或者晚安语录

### 本代码文章首发于公众号「Python知识圈」，如需转载，请通过公众号联系作者pk哥，谢谢

![公众号](https://github.com/Brucepk/pk.github.io/blob/master/gzh.jpg)

#### 公众号里提供了我的微信，可以联系到我。


昨天在技术群里问大家七夕节礼物准备好了吗？大多数男程序员回复姿势都是这样的：

> 程序员有女朋友？

> new 一个就行。

> Python 只要内存够，想 new 多少个对象都不是问题。

由于行业环境的原因，程序员单身的确实多，这也是程序员的世纪难题。

今天，不是给大家发对象，只教大家方法。今天教大家怎么用 Python 给心动的人每天定时发早安或者晚安。

前提条件是，你得有一个心动对象。哇，我连心动对象都没有怎么办？骚年，那你还不赶紧行动，去寻找你的心动的 TA。

好了，直接进入今天的主题。

#### 找对象环境
语言：Python3
编辑工具：Pycharm

#### 导包
wxpy：操作微信的库，机器人陪你唠嗑那篇文章也用到过。

requests：用来请求目标网站。

Timer：定时器，是 Thread 的派生类，用于在指定时间后调用一个方法。

from wxpy import *
import requests
from threading import Timer
#### 登录微信
Bot 对象，用于登陆和操作微信账号，涵盖大部分 Web 微信的功能。cache_path，设置当前会话的缓存路径，并开启缓存功能，为 None (默认) 则不开启缓存功能。开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。设为 True 时，使用默认的缓存路径 「wxpy.pkl」。

bot = Bot(cache_path=True)
#### 获取语句
从金山词霸每日一句接口获取语录，用 requests 请求 api 地址，返回英文美句和中文翻译。

### 原文请 [点击这里查看](https://mp.weixin.qq.com/s?__biz=MzU4NjUxMDk5Mg==&mid=2247484070&idx=1&sn=a65857516d1cccda20ac7aacb148a0c1&scene=19#wechat_redirect)
