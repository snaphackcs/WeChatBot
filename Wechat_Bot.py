import sys
import time
import ntchat

from json import load, dump
from time import time
from shutil import rmtree
from os import system
from re import sub

from Sign import sign
from Setu import random_setu, time_convert


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
with open("info.json", mode="r", encoding="utf-8") as f:
    origin = load(f)

# print(name_dict)
# print(wechat.get_contacts())

# 提醒群友bot已经启动
wechat.send_text(to_wxid="23278031443@chatroom", content="bot已启动，已更新称号！ ᕕ( ᐛ )ᕗ")


@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def bot(wechat_instance: ntchat.WeChat, message):
    global setu_time
    global name_dict
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]
    if room_wxid == "23278031443@chatroom":
        from_wxid = data["from_wxid"]
        # 签到
        if msg == "/sign":
            print(sign(from_wxid))
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=sign(from_wxid), at_list=[from_wxid])

        # 跑团
        elif msg[:5] == "/roll":
            msg = sub(r'[\/\\\"\<\>\|\_\%\;\']', "/", msg)
            print(f"python Command.py {msg}")
            system(f"python Command.py {msg}")
            with open("temp.json", mode="r", encoding="utf-8") as doc:
                wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                                 content=f"@{name_dict[from_wxid]} {load(doc)['text']} ᕕ( ᐛ )ᕗ",
                                                 at_list=[from_wxid])

        # 瑟瑟
        elif msg[:5] == "/setu":
            if time() - int(origin['last_setu']) >= 7200:
                msg = sub(r'[\/\\\"\<\>\|\_\%\;\']', "/", msg[5:])
                system(f"python Command.py {msg}")
                data = random_setu()
                wechat_instance.send_text(to_wxid="23278031443@chatroom", content="啊哈哈哈！色图来喽！ᕕ( ᐛ )ᕗ")
                for img in data:
                    print(img)
                    # wechat_instance.send_image(to_wxid="23278031443@chatroom", file_path=img)
                origin['last_setu'] = time()
                with open("info.json", mode="w") as doc:
                    dump(origin, doc, indent=4)
                time.sleep(1)
                rmtree("temp")  # 清除缓存

            else:
                wechat_instance.send_text(to_wxid="23278031443@chatroom",
                                          content=f"贤者时间还有{time_convert(7200 - time() + int(origin['last_setu']))}，"
                                                  f"先休息一下啦(｀Д´)")


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
