import random
from json import load
from BuildArchives import new_archive

def roll(from_wxid, msg):
    # 读取人名列表
    with open("name_dict.json", mode="r", encoding="utf-8") as f:
        name_dict = load(f)
    # 读取账户列表
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)

    # 建档
    if from_wxid not in origin.keys():
        new_archive(from_wxid)

    dice = eval(msg[5::])
    return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 投了一个d{dice}，结果是{random.randint(1, dice)}ᕕ( ᐛ )ᕗ"


if __name__ == '__main__':
    print(roll("wxid_pdb55y5c8l5n12","/roll6"))
