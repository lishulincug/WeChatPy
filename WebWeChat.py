#!/usr/local/bin/python3
# coding: utf-8
# 导入模块

from wxpy import *
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 初始化机器人，扫码登陆
def login_callback():
    print("登录成功...")
    os.system("say web微信自动登录成功")

def logout_callback():
    print("登出成功...")
    os.system("say web微信离线")

bot = Bot(console_qr=False,login_callback=login_callback(),logout_callback=logout_callback(),cache_path=True)



def first_login_send():
    mp_zsyh = bot.mps().search('招商银行信用卡');
    if mp_zsyh is not None and len(mp_zsyh)>0:
        mp_zsyh[0].send('签到');
    else:
        print("没有这个公众号")

# bot.add_friend('tianzhidao28','我是WaterXu');

# 打印来自其他好友、群聊和公众号的消息
@bot.register(msg_types=(TEXT,VIDEO))
def print_others(msg):
    print(msg)


# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    print(msg)
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

# 堵塞线程，并进入 Python 命令行

bot.auto_mark_as_read = True
first_login_send();

# 或者仅仅堵塞线程
bot.join();