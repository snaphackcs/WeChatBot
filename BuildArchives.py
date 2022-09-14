from json import load


def new_archive(from_wxid):
    # 读取人名列表
    with open("name_dict.json", mode="r", encoding="utf-8") as f:
        name_dict = load(f)
    # 读取账户列表
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)

    # 建档
    if from_wxid not in origin.keys():
        if from_wxid not in name_dict.keys():
            new_info_json = {from_wxid: "*姓名未录入*"}  # TODO: 读取群昵称
            name_dict.update(new_info_json)

        new_info_json = {from_wxid: {
            "name": name_dict[from_wxid],
            "score": 0,
            "sign_or_not": False,
            "title": ""
        }}
        origin.update(new_info_json)