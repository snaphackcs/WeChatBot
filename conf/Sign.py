from json import load, dump
from datetime import datetime
from BuildArchives import new_archive
from math import log10


def sign(from_wxid):
    # 读取账户列表
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)

    # 更新现在的时间
    if datetime.now().strftime("%Y%m%d") != origin["date"]:
        origin["date"] = datetime.now().strftime("%Y%m%d")
        for key in origin.keys():
            if key in ["date", "last_setu"]:
                continue
            if origin[key]["sign_or_not"] and "sign_days" in origin[key].keys():
                origin[key]["sign_days"] += 1
            else:
                origin[key]["sign_days"] = 1
            origin[key]["sign_or_not"] = False
            origin[key]["fortune"] = 0

    # 判断是否已签到并输出
    if origin[from_wxid]["sign_or_not"]:
        print(origin[from_wxid]["sign_or_not"])
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经签过了(｀Д´)，算力为{origin[from_wxid]['score']}点"

    origin[from_wxid]["score"] += int(log10(origin[from_wxid]["sign_days"]) * 10 + 5)
    origin[from_wxid]["sign_or_not"] = True
    with open("info.json", mode="w") as f:
        dump(origin, f, indent=4)
    return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 签到成功ᕕ( ᐛ )ᕗ，" \
           f"你已经连续签到{origin[from_wxid]['sign_days']}天啦！今日算力+={int(log10(origin[from_wxid]['sign_days']) * 10 + 5)}，" \
           f"总算力为{origin[from_wxid]['score']}点~"


if __name__ == '__main__':
    print(sign("wxid_f42f8bssyu9312"))
