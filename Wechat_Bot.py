import sys
import time
from datetime import datetime
from json import load, dump
from time import time
import ntchat
from Sese import RandomSetu
from shutil import rmtree
from time import sleep
from os import system
from re import sub, compile

# 替换字符
pattern = compile(r'[\/\\\"\<\>\|\_\%\;\']')
# 创建微信
wechat = ntchat.WeChat()
# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)
# 等待登录
wechat.wait_login()
# 色图冷却计时器，防止有老六访问量过大
setu_time = 0
# 贤者时间语句计时器
xianzhe_time = 0
# 读取群友信息
with open("name_dict.json", mode="r", encoding="utf-8") as f:
    name_dict = load(f)
print(name_dict)
# 提醒群友bot已经启动
wechat.send_text(to_wxid="23278031443@chatroom", content="bot已启动，目前支持发色图和签到哦 ᕕ( ᐛ )ᕗ")


# 监测到有人发了消息
@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
# 用于发色图的函数
def send_setu(wechat_instance: ntchat.WeChat, message):
    # 利用全局变量来读取两个计时器的值
    global pattern
    global setu_time
    global xianzhe_time
    # 获取群中消息的信息
    data = message["data"]
    # 获取信息的具体内容
    msg = data["msg"]
    # 获取消息是在哪一个群
    room_wxid = data["room_wxid"]
    # 判断是否在SnapHack群使用的色图指令
    if room_wxid == "23278031443@chatroom" and msg.split(" ")[0] == "/setu" and time() - setu_time >= 3:
        # 如果已经过了贤者时间
        if time() - setu_time >= 180:
            msg = sub(pattern, "/", msg[5::])
            system(f"python SetuConfig.py{msg}")
            # 将计时器更新到现在的时间
            setu_time = time()
            # 爬取色图同时获取色图信息
            data = RandomSetu()
            # 利用循环将所有访问到的色图全部发出去
            for img in data:
                print(img)
                wechat_instance.send_image(to_wxid="23278031443@chatroom", file_path=img)
            sleep(1)
            # 递归删除色图, 释放内存ᕕ( ᐛ )ᕗ
            rmtree("temp")
        # 如果没有过贤者时间但是过了发送贤者时间冷却
        elif time() - xianzhe_time >= 1.5:
            # 将计时器更新到现在的时间
            xianzhe_time = time()
            # 输出贤者时间
            wechat_instance.send_text(to_wxid="23278031443@chatroom",
                                      content=f"贤者时间还有{'%.2f' % (180 - time() + setu_time)}秒")


@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def sign(wechat_instance: ntchat.WeChat, message):
    global name_dict
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]
    from_wxid = data["from_wxid"]
    if room_wxid == "23278031443@chatroom" and msg.lower() == "/sign":
        with open("info.json", mode="r", encoding="utf-8") as f:
            origin = load(f)
        if datetime.now().strftime("%Y%m%d") != origin["date"]:
            origin["date"] = datetime.now().strftime("%Y%m%d")
            for key in origin.keys():
                if key == "date":
                    continue
                origin[key]["sign_or_not"] = False
        if from_wxid not in origin.keys():
            if from_wxid in name_dict.keys():
                new_info_json = {from_wxid: {
                    "name": name_dict[from_wxid],
                    "score": 1,
                    "sign_or_not": True,
                    "title": ""
                }}
                origin.update(new_info_json)
                wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                                 content=f"@{origin[from_wxid]['name']} 签到成功ᕕ( ᐛ )ᕗ, 只因分加1, 为{origin[from_wxid]['score']}分",
                                                 at_list=[from_wxid])
            else:
                wechat_instance.send_text(to_wxid="23278031443@chatroom", content="还在建档中别急啊(っ*´Д`)っ")
        elif not origin[from_wxid]["sign_or_not"]:
            origin[from_wxid]["score"] += 1
            origin[from_wxid]["sign_or_not"] = True
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=f"@{origin[from_wxid]['name']} 签到成功ᕕ( ᐛ )ᕗ, 只因分加1, 为{origin[from_wxid]['score']}分",
                                             at_list=[from_wxid])
        else:
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=f"@{origin[from_wxid]['name']} 你已经签过了(｀Д´), 为{origin[from_wxid]['score']}分",
                                             at_list=[from_wxid])
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
