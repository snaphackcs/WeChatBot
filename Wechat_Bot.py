import sys
import time
from json import load
from time import time
import ntchat
from SetuConfig import randomSetu, time_convert
from shutil import rmtree
from time import sleep
from os import system
from re import sub, compile
from Sign import sign

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
# wechat.send_text(to_wxid="23278031443@chatroom", content="bot已启动，目前支持发色图和签到哦 ᕕ( ᐛ )ᕗ")

@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def bot(wechat_instance: ntchat.WeChat, message):
    global setu_time
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]
    if room_wxid == "23278031443@chatroom":
        from_wxid = data["from_wxid"]
        # 签到
        if msg == "/sign":
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=sign(from_wxid), at_list=[from_wxid])

        # 瑟瑟
        elif msg[:5] == "/setu":
            if time() - setu_time >= 7200:
                msg = sub(pattern, "/", msg[5:])
                system(f"python SetuConfig.py{msg}")
                setu_time = time()
                data = randomSetu()
                for img in data:
                    print(img)
                    wechat_instance.send_image(to_wxid="23278031443@chatroom", file_path=img)
                sleep(1)
                rmtree("temp")  #清除缓存
            else:
                wechat_instance.send_text(to_wxid="23278031443@chatroom",
                                          content=f"贤者时间还有{time_convert(7200 - time() + setu_time)}")


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
