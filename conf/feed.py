
from json import load, dump
#框架大体实现 背包目前很多没有对应的项是准备添加的
with open("config/bao.json", mode="r", encoding="utf-8") as f:
    #背包 应该把favor移到info里
    bao = load(f)
with open("config/favor.json", mode="r", encoding="utf-8") as s:
    #不同好感度回复
    fav = load(s)
with open("config/wuping.json", mode="r", encoding="utf-8") as t:
    #物品储存值于中文转换
    wuping = load(t)


def touwei(wechat, msg, wxid, room):
    global bao
    global fav
    global wuping
    gift = []
    print("touweiwork")
    for item in bao[wxid]:
        #循环背包物品，匹配关键词确定投喂的物品
        print("append")
        #判断拥有数量大于0并且在发送到消息里出现过
        if bao[wxid][item] > 0 and (wuping[item] in msg):
            print("appednwork")
            gift.append(item)
    #如果只有一个关键词则完成投喂
    if len(gift) == 1:
        print('giftwork')
        bao[wxid][gift[0]] -= 1
        bao[wxid]["favor"] += 5
        with open("config/bao.json", mode="w") as r:
            dump(bao, r, indent=4)
        for key in fav[gift[0]]:
            print(key)
            #对比好感度，以及投喂物品不同语音的好感度
            if bao["wxid_ssyd5nc3hbcp12"]["favor"] <= int(key):
                print("compared")
                wechat.send_room_at_msg(to_wxid=room,
                                        content=f"{fav[gift[0]][key]}", at_list=[wxid])
                return

    if len(gift) >= 2:
        wechat.send_room_at_msg(to_wxid=room,
                                content=f"@你到底要给本bot投喂什么呀",
                                at_list=[wxid])
        return

    else:
        print("elsework")
        wechat.send_room_at_msg(to_wxid=room,
                                content=r"@你确定？/n你貌似没有呢，",
                                at_list=[wxid])
        return
