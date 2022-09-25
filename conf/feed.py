import ntchat
from json import load,dump


wechat = ntchat.WeChat()
with open("config/bao.json", mode="r", encoding="utf-8") as f:
    bao = load(f)
with open("config/favor.json", mode="r", encoding="utf-8") as f:
    fav = load(f)
def touwei(msg,wxid,room):
    global bao
    global fav
    gift=[]

    for item in bao[wxid]:
        if msg.contains(bao[wxid][item]):
            gift.append(item)

    if len(gift)==1:
        bao[wxid][gift[0]]-=1
        bao[wxid]["favor"]+=5
        for key in fav[gift[0]]:
            print(key)
            if bao["wxid_ssyd5nc3hbcp12"]["favor"] > int(key):
                wechat.send_room_at_msg(to_wxid=room,
                                        content=f"{fav[gift][key]}",
                                        at_list=[wxid])
        with open("config/info.json", mode="w") as f:
            dump(bao, f, indent=4)
        return

    if len(gift)>=2:
        wechat.send_room_at_msg(to_wxid=room,
                                content=f"@你到底要给本bot投喂什么呀",
                                at_list=[wxid])
        return

    else:
        wechat.send_room_at_msg(to_wxid=room,
                                content=r"@你确定？\n你貌似没有呢，",
                                at_list=[wxid])
        return


