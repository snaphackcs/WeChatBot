import argparse
from json import dump

tag = []
parser = argparse.ArgumentParser()
parser.add_subparsers()
parser.add_argument("-R", "--r18", type=int, choices=[0, 1], default=0, help="0不为R18，1为R18")
parser.add_argument("-N", "--num", type=int, choices=range(1, 21), default=1, help="爬取图片数目，在1到20之间")
parser.add_argument("-T", "--tag", default="", nargs='*')
args = vars(parser.parse_args())
for i in args["tag"]:
    s = "".join(f"{j}|" for j in i.split("/"))
    tag.append(s)

default_json = {"r18": args["r18"], "num": args["num"], "tag": tag}

print(default_json)
with open("config.json", mode="w") as f:
    dump(default_json, f, indent=4)