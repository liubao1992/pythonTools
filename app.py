from flask import Flask
import pyautogui
import pyperclip
import time
# from __future__ import unicode_literals
from wxpy import *
import requests
from wechat_sender import Sender

app = Flask(__name__)
def autoclick():
    contents = """ 
        zhe
        shi 
        yi
        ge
        ce
        shi 
        chen
        xu
        """
    for line in contents.split("\n"):
        if line:
            print(line)
            # 模拟点击鼠标位置
            pyautogui.click(502, 870)
            # copy剪切板
            pyperclip.copy(line)
            pyautogui.hotkey("Ctrl", "v")
            pyautogui.typewrite("\n")
            # pyautogui.press('enter')
            time.sleep(1)
#autoclick()

bot = Bot(cache_path=True)#登录微信，扫一下弹出来的二维码然后同意即可

def get_news1():
    # 获取txt文件数据(需要轰炸的信息，一行一条)
    file = open("1.txt")  #
    get = file.read()
    result = get.splitlines()
    return result

def send_news():
    try:
        my_friend = bot.friends().search(u'lb738615')[0]  # 你朋友的微信昵称（不是备注，微信帐号）
        for i in range(len(message_text)):
            my_friend.send(message_text[i])
            time.sleep(0.5)  # 0.5秒发送一条，直到全部发完
    except:
        my_friend = bot.friends().search('bao4996870')[0]  # 你的微信昵称（不是微信帐号）
        my_friend.send(u"消息发送失败")


# @app.route('/')
# def hello_world():
#     time.sleep(5)
#
#     return 'Hello, World!'


if __name__ == '__main__':
    message_text = get_news1()
    send_news()
    app.run(port=5500, host='0.0.0.0', debug=True)
