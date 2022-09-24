import json
import ntchat
from pprint import pprint


def love(wechat_instance: ntchat.WeChat, message):
    from_wxid = message["data"]["from_wxid"]
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = json.load(f)
    if "love" not in origin[from_wxid].keys():
        origin[from_wxid]["love"] = 0

    with open("info.json", mode="w", encoding="utf-8") as f:
        json.dump(origin, f, indent=4)
    wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                     content=f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你的机器人好感度是 {origin[from_wxid]['love']}",
                                     at_list=[from_wxid])


def bixin(wechat_instance: ntchat.WeChat, message):
    print(1)
    from_wxid = message["data"]["from_wxid"]
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = json.load(f)
    if "love" not in origin[from_wxid].keys():
        origin[from_wxid]["love"] = 0
    if origin[from_wxid]['score'] >= 10:
        origin[from_wxid]['love'] += 5
        origin[from_wxid]['score'] -= 10
        wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                         content=f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 恭喜你购买并送出了笔芯",
                                         at_list=[from_wxid])
        wechat_instance.send_text(to_wxid="23278031443@chatroom",
                                  content=f"是笔芯欸，我收到了哦")


    else:
        wechat_instance.send_room_at_msg(to_wxid="23278031443@chatroom",
                                         content=f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你没有足够的积分哦",
                                         at_list=[from_wxid])
    with open("info.json", mode="w", encoding="utf-8") as f:
        json.dump(origin, f, indent=4)


if __name__ == '__main__':
    love("kanghaotian")
