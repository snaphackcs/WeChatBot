import argparse
from json import dump
from commands.Roll import roll
from commands.Change import chag

# 色图函数
def setu_config(args):
    tag = []
    for i in args["tag"]:
        s = "".join(f"{j}|" for j in i.split("/"))
        tag.append(s)
    default_json = {"r18": args["r18"], "num": args["num"], "tag": tag}
    print(default_json)
    with open("config/config.json", mode="w") as f:
        dump(default_json, f, indent=4)


# 创建最高等级的命令行
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
subparsers.required = True

# 创建色图命令行
parser_setu = subparsers.add_parser("/setu", help="设置色图参数")
parser_setu.add_argument("-R", "--r18", type=int, choices=[0, 1], default=0, help="0不为R18，1为R18")
parser_setu.add_argument("-N", "--num", type=int, choices=range(1, 21), default=1, help="爬取图片数目，在1到20之间")
parser_setu.add_argument("-T", "--tag", default="", nargs='*')
parser_setu.set_defaults(func=setu_config)

# 创建随机数函数
parser_roll = subparsers.add_parser("/roll")
parser_roll.add_argument("-D", "--dice", type=int, default=6)
parser_roll.add_argument("-N", "--num", type=int, default=1)
parser_roll.set_defaults(func=roll)

parser_chag = subparsers.add_parser("/chag")
parser_chag.add_argument("-D", "--day", type=int, default=1)
parser_chag.add_argument("-P", "--point", type=int, default=1)
parser_chag.add_argument("-U", "--user", type=str, default="wxid_pdb55y5c8l5n12")
parser_chag.set_defaults(func=chag)
start = parser.parse_args()

# 执行函数功能
start.func(vars(parser.parse_args()))
