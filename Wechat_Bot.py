import sys
import time
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
wechat.send_text(to_wxid="wxid_pdb55y5c8l5n12", content="setu")


@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def send_setu(wechat_instance: ntchat.WeChat, message):
    global setu_time
    global xianzhe_time
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["to_wxid"]
    if room_wxid == "23278031443@chatroom" and msg.lower() == "setu" or msg.lower() == "涩涩" or msg.lower() == "色色" \
            or msg.lower() == "色图" or msg.lower() == "sese":
        if time() - setu_time >= 180:
            setu_time = time()
            data = RandomSetu()
            for img in data[0]:
                print(img)
                wechat_instance.send_image(to_wxid="23278031443@chatroom", file_path=img)
            if data[1]:
                wechat_instance.send_text(to_wxid="23278031443@chatroom", content="有些图被bot ban了, 不怪我ᕕ( ᐛ )ᕗ")
                sleep(1)
            # 递归删除色图, 释放内存ᕕ( ᐛ )ᕗ
            rmtree("temp")
        elif time() - xianzhe_time >= 1.5:
            xianzhe_time = time()
            wechat_instance.send_text(to_wxid="23278031443@chatroom",
                                      content=f"贤者时间还有{'%.2f' % (180 - time() + setu_time)}秒")


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
