
import ntchat
import time
import sys

import conf

functions = conf.functions

wechat = ntchat.WeChat()

wechat.open(smart=True)

wechat.wait_login()

@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
def bot(wechat_instance: ntchat.WeChat, message):
    global functions

    data = message["data"]
    msg = data["msg"]
    room_wxid = data["room_wxid"]

    if msg in functions:
        functions[msg](wechat_instance, message)
    else:
        print("no message")
        time.sleep(1)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()