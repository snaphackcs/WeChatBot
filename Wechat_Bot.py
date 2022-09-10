import sys
import time
from datetime import datetime
from json import load, dump
from time import time
import ntchat
from Sese import RandomSetu
from shutil import rmtree
from time import sleep

# 创建微信
wechat = ntchat.WeChat()
# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)
# 等待登录
wechat.wait_login()
# 发信息冷却
setu_time = 0
xianzhe_time = 0
last_path = ""
with open("name_dict.json", mode="r", encoding="utf-8") as f:
    name_dict = load(f)
print(name_dict)
wechat.send_text(to_wxid="23278031443@chatroom", content="bot已启动，目前支持发色图和签到哦 ᕕ( ᐛ )ᕗ")


@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def send_setu(wechat_instance: ntchat.WeChat, message):
    global setu_time
    global xianzhe_time
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]
    if room_wxid == "23278031443@chatroom" and msg.lower() == "/setu":
        if time() - setu_time >= 180:
            setu_time = time()
            data = RandomSetu()
            request_times = 0
            while len(data[0]) == 0 and request_times < 10:
                data = RandomSetu()
                request_times += 1
            for img in data[0]:
                print(img)
                wechat_instance.send_image(to_wxid="23278031443@chatroom", file_path=img)
            if data[1]:
                wechat_instance.send_text(to_wxid="23278031443@chatroom", content="有些图被bot ban了, 不怪我 ᕕ( ᐛ )ᕗ")
                sleep(1)
            # 递归删除色图, 释放内存ᕕ( ᐛ )ᕗ
            rmtree("temp")
        elif time() - xianzhe_time >= 1.5:
            xianzhe_time = time()
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
