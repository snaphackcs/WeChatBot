from json import load, dump


def new_archive(from_wxid):
    # 读取人名列表
    with open("config/name_dict.json", mode="r", encoding="utf-8") as f:
        name_dict = load(f)
    # 读取账户列表
    with open("config/info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)
    with open("config/bao.json",mode="r",encoding="utf-8") as f:
        bao=load(f)
    # 建档
    if from_wxid not in origin.keys():
        if from_wxid not in name_dict.keys():
            new_info_json = {from_wxid: "*姓名未录入*"}  # TODO: 读取群昵称
            name_dict.update(new_info_json)
            with open("config/name_dict.json", mode="w") as f:
                dump(name_dict, f, indent=4)
        new_info_json = {from_wxid: {
            "name": name_dict[from_wxid],
            "score": 0,
            "sign_or_not": False,
            "fortune":0,
            "title": "",
            "sign_days": 1
        }}
        new_inven_json={from_wxid: {
            "favor":0,
            "fish1": 0,
            "fish2": 0,
            "nvzhuang": 0,
            "shezhang": 0,
            "qilunuo": 0,
            "pink_flower": 0,
            "blue_flower": 0,
            "wine": 0,
            "tea": 0,
            "panc": 0,
            "cake": 0,
            "apple": 0,
            "ch_cake": 0,
            "french": 0,
            "pding": 0,
            "parfait": 0,
            "waffle": 0
        }}
        origin.update(new_info_json)
        bao.update(new_inven_json)
        with open("config/info.json", mode="w") as f:
            dump(origin, f, indent=4)
        with open("config/bao.json", mode="w") as f:
            dump(origin, f, indent=4)
