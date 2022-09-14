from json import load,dump
from datetime import datetime
from BuildArchives import new_archive


def sign(from_wxid):
    # 读取人名列表
    with open("name_dict.json", mode="r", encoding="utf-8") as f:
        name_dict = load(f)
    # 读取账户列表
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)

    # 更新现在的时间
    if datetime.now().strftime("%Y%m%d") != origin["date"]:
        origin["date"] = datetime.now().strftime("%Y%m%d")
        for key in origin.keys():
            if key == "date":
                continue
            origin[key]["sign_or_not"] = False

    # 建档
    if from_wxid not in origin.keys():
        new_archive(from_wxid)

    # 判断是否已签到并输出
    if not origin[from_wxid]["sign_or_not"]:
        origin[from_wxid]["score"] += 1
        origin[from_wxid]["sign_or_not"] = True
        with open("info.json", mode="w") as f:
            dump(origin, f, indent=4)
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 签到成功ᕕ( ᐛ )ᕗ, 算力++, 为{origin[from_wxid]['score']}点"

    else:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你已经签过了(｀Д´), 算力为{origin[from_wxid]['score']}点"

if __name__ == '__main__':
    print(sign("wxid_f42f8bssyu9312"))