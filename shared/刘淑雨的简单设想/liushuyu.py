import ntchat

def liushuyu(wechat_instance: ntchat.WeChat, message):
    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]