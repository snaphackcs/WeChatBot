import sys
import time
import ntchat
from os.path import join
from json import load, dump
from time import time, localtime, sleep
from os import system, getcwd
from re import sub
from BuildArchives import new_archive
from Fortuneslip import fortune, slip
from Sign import sign
from Setu import random_setu, time_convert
from Fish import fish
from meitu import erciyuan
from Joke import joke
import random
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
lastmoyu=0
moyutime=0
# 读取群友信息
with open("name_dict.json", mode="r", encoding="utf-8") as f:
    name_dict = load(f)
with open("info.json", mode="r", encoding="utf-8") as f:
    origin = load(f)


# 提醒群友bot已经启动
# wechat.send_text(to_wxid="23278031443@chatroom", content="bot已启动，已更新钓鱼！ ᕕ( ᐛ )ᕗ")


@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def bot(wechat_instance: ntchat.WeChat, message):
    global setu_time
    global name_dict
    global origin
    global name_dict
    global moyutime
    global lastmoyu
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]

    # 判断是否是SnapHack群消息
    if room_wxid == "23278031443@chatroom":
        from_wxid = data["from_wxid"]
        # 判断是否已经建档
        if from_wxid not in origin.keys():
            new_archive(from_wxid)
            with open("info.json", mode="r", encoding="utf-8") as f:
                origin = load(f)
            with open("name_dict.json", mode="r", encoding="utf-8") as f:
                name_dict = load(f)

        # 签到
        if msg == "/sign":
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=sign(from_wxid), at_list=[from_wxid])

        # 今日人品
        if msg == "/fortune":
            if slip(from_wxid):
                slippath = [join(getcwd(), "slip.gif").replace("\\", "/")]
                wechat_instance.send_gif(to_wxid="23278031443@chatroom", file=slippath[0])
            sleep(2)
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=fortune(from_wxid), at_list=[from_wxid])

        if msg == "/time":
            timetu=[join(getcwd(), f"time\\{localtime()[3]}.gif").replace("\\", "/")]
            wechat.send_gif(to_wxid="23278031443@chatroom", file=timetu[0])

        # 钓鱼
        if msg == "/fish":
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                             content=fish(from_wxid), at_list=[from_wxid])

        if msg == "/flip_coin":
            if random.randint(0,1)==1:
                wechat.send_gif(to_wxid="23278031443@chatroom", file=r"C:\WeChatBot\1.gif")
            else:
                wechat.send_gif(to_wxid="23278031443@chatroom", file=r"C:\WeChatBot\hua.gif")

        # 地狱笑话
        if msg == "/joke":
            wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom", content=joke(from_wxid), at_list=[from_wxid])

        if msg=="/test":
            wechat_instance.send_video(to_wxid="23278031443@chatroom",file_path=r"C:\WeChatBot\test.mp3")

        if msg=="/rick_roll":
            wechat_instance.send_video(to_wxid="23278031443@chatroom", file_path=r"C:\WeChatBot\rickroll.mp4")

        # 跑团
        elif msg[:5] == "/roll":
            msg = sub(r'[\\\"\<\>\|\']', "/", msg)
            print(f"python Command.py {msg}")
            system(f"python Command.py {msg}")
            with open("temp.json", mode="r", encoding="utf-8") as doc:
                wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                                 content=f"@{name_dict[from_wxid]} {load(doc)['text']} ᕕ( ᐛ )ᕗ",
                                                 at_list=[from_wxid])
        elif msg[:5] == "/chag":
            msg = sub(r'[\\\"\<\>\|\']', "/", msg)
            with open("temp.json", mode="w") as doc:
                dump({"wxid": f"{from_wxid}"}, doc, indent=4)
            print(f"python Command.py {msg}")
            system(f"python Command.py {msg}")


        # 瑟瑟
        elif msg[:5] == "/setu":
            if time() - int(origin['last_setu']) >= 7200:
                msg = sub(r'[\/\\\"\<\>\|\_\%\;\']', "/", msg[5:])
                system(f"python Command.py {msg}")
                data = random_setu()
                wechat_instance.send_text(to_wxid="23278031443@chatroom", content="啊哈哈哈！色图来喽！ᕕ( ᐛ )ᕗ")
                for img in data:
                    print(img)
                    wechat_instance.send_image(to_wxid="23278031443@chatroom", file_path=img)
                origin['last_setu'] = time()
                with open("info.json", mode="w") as doc:
                    dump(origin, doc, indent=4)
            else:
                wechat_instance.send_text(to_wxid="23278031443@chatroom",
                                          content=f"贤者时间还有{time_convert(7200 - time() + int(origin['last_setu']))}，"
                                                  f"先休息一下啦(｀Д´)")

        elif from_wxid=="wxid_ssyd5nc3hbcp12" and msg[:1] == "/":
                wechat_instance.send_text(to_wxid="23278031443@chatroom", content=msg)





try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
