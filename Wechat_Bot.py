import sys
import time
import ntchat
from os.path import join
from json import load, dump
from time import time, localtime, sleep
from os import system, getcwd
from re import sub
from src.BuildArchives import new_archive
from conf.Fortuneslip import fortune, slip
from conf.Sign import sign
from commands.Setu import random_setu, time_convert
from conf.Fish import fish
from conf.meitu import erciyuan
from conf.Joke import joke
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
with open("config/name_dict.json", mode="r", encoding="utf-8") as f:
    name_dict = load(f)
with open("config/info.json", mode="r", encoding="utf-8") as f:
    origin = load(f)
with open("config/room.json", mode="r", encoding="utf-8") as f:
    room = load(f)
with open("config/bao.json", mode="r", encoding="utf-8") as f:
    bao = load(f)
with open("temp.json", mode="w") as f:
    tp = load(f)
# 提醒群友bot已经启动
# wechat.send_text(to_wxid=room_wxid, content="bot已启动，已更新钓鱼！ ᕕ( ᐛ )ᕗ")


@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def bot(wechat_instance: ntchat.WeChat, message):
    global setu_time
    global name_dict
    global origin
    global name_dict
    global moyutime
    global lastmoyu
    global room
    global tp
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]

    # 判断是否是SnapHack群消息
    if room[room_wxid]:
        from_wxid = data["from_wxid"]
        # 判断是否已经建档
        if from_wxid not in origin.keys():
            new_archive(from_wxid)
            with open("config/info.json", mode="r", encoding="utf-8") as f:
                origin = load(f)
            with open("config/name_dict.json", mode="r", encoding="utf-8") as f:
                name_dict = load(f)

        # 签到
        if msg == "/sign":
            wechat_instance.send_room_at_msg(to_wxid=room_wxid,
                                             content=sign(from_wxid), at_list=[from_wxid])

        # 今日人品
        if msg == "/fortune":
            if slip(from_wxid):
                slippath = [join(getcwd(), "img\\slip.gif").replace("\\", "/")]
                wechat_instance.send_gif(to_wxid=room_wxid, file=slippath[0])
            sleep(2)
            wechat_instance.send_room_at_msg(to_wxid=room_wxid,
                                             content=fortune(from_wxid), at_list=[from_wxid])

        if msg == "/time":
            timetu=[join(getcwd(), f"img\\time\\{localtime()[3]}.gif").replace("\\", "/")]
            wechat.send_gif(to_wxid=room_wxid, file=timetu[0])

        # 钓鱼
        if msg == "/fish":
            wechat_instance.send_room_at_msg(to_wxid=room_wxid,
                                             content=fish(from_wxid), at_list=[from_wxid])

        if msg == "/flip_coin":
            if random.randint(0,1)==1:
                wechat.send_gif(to_wxid=room_wxid, file=r"C:\WeChatBot\1.gif")
            else:
                wechat.send_gif(to_wxid=room_wxid, file=r"C:\WeChatBot\hua.gif")
        if msg == "/b":
            item=""
            for itemt in range(bao[from_wxid]):
                if bao[from_wxid][itemt]!=0:
                    item+=(f"{itemt}:{bao[from_wxid][itemt]}个")
                    item+=(r"\n")
            wechat_instance.send_room_at_msg(to_wxid=room_wxid,
                                             content=item, at_list=[from_wxid])



        # 地狱笑话
        if msg == "/joke":
            wechat_instance.send_room_at_msg(to_wxid=room_wxid, content=joke(from_wxid), at_list=[from_wxid])


        if msg == "/二次元":
            if moyutime >= 3 and random.randint(0, 1):
                wechat_instance.send_room_at_msg(to_wxid=room_wxid,
                                                 content=f"@{name_dict[from_wxid]} 崽啊，都已经几点了",
                                                 at_list=[from_wxid])
                sleep(1)
                wechat_instance.send_text(to_wxid=room_wxid, content="还在玩机器人")
                sleep(1)
                wechat_instance.send_text(to_wxid=room_wxid, content="我该怎么说你好")
                sleep(1)
                wechat_instance.send_text(to_wxid=room_wxid, content="再不爬起来写作业")
                sleep(1)
                wechat_instance.send_text(to_wxid=room_wxid, content="妈给你一拳")
                yiquan = [join(getcwd(), f"img/kekeluo_punch.jpg").replace("\\", "/")]
                wechat_instance.send_image(to_wxid=room_wxid, file_path=yiquan[0])
                moyutime = 0
            else:
                if (time() - lastmoyu) < 300:
                    moyutime += 1
                else:
                    moyutime = 0
                wechat_instance.send_image(to_wxid=room_wxid, file_path=erciyuan()[0])
                lastmoyu = time()

        # 跑团
        elif msg[:5] == "/roll":
            msg = sub(r'[\\\"\<\>\|\']', "/", msg)
            print(f"python src/Command.py {msg}")
            system(f"python src/Command.py {msg}")
            with open("temp.json", mode="r", encoding="utf-8") as doc:
                wechat_instance.send_room_at_msg(to_wxid=room_wxid,
                                                 content=f"@{name_dict[from_wxid]} {load(doc)['text']} ᕕ( ᐛ )ᕗ",
                                                 at_list=[from_wxid])
        elif msg[:5] == "/chag":
            msg = sub(r'[\\\"\<\>\|\']', "/", msg)
            with open("temp.json", mode="w") as doc:
                dump({"wxid": f"{from_wxid}"}, doc, indent=4)
            print(f"python src/Command.py {msg}")
            system(f"python src/Command.py {msg}")


        # 瑟瑟
        elif msg[:5] == "/setu":
            if time() - int(origin['last_setu']) >= 7200 or room_wxid=="25408612857@chatroom":
                msg = sub(r'[\/\\\"\<\>\|\_\%\;\']', "/", msg[5:])
                system(f"python Command.py {msg}")
                data = random_setu()
                wechat_instance.send_text(to_wxid=room_wxid, content="啊哈哈哈！色图来喽！ᕕ( ᐛ )ᕗ")
                for img in data:
                    print(img)
                    wechat_instance.send_image(to_wxid=room_wxid, file_path=img)
                origin['last_setu'] = time()
                with open("config/info.json", mode="w") as doc:
                    dump(origin, doc, indent=4)
            else:
                wechat_instance.send_text(to_wxid=room_wxid,
                                          content=f"贤者时间还有{time_convert(7200 - time() + int(origin['last_setu']))}，"
                                                  f"先休息一下啦(｀Д´)")






try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
