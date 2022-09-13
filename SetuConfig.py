import argparse
from json import load
from os.path import exists, join
from requests import get
from pprint import pprint
from os import mkdir, getcwd, system
from json import dump

# 爬虫函数
def randomSetu():
    path_list = []
    # 新建文件夹
    if not exists(r".\temp"):
        mkdir("temp")
    # 新建原始json
    if not exists("config.json"):
        default_json = {
            "r18": 0,
            "num": 1,
            "uid": None,
            "tag": []
        }
        with open("config.json", mode="w") as f:
            dump(default_json, f, indent=4)
    # headers用于伪装成浏览器爬取图片
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 '
                      'Safari/537.36 '
    }
    # 打开json文件
    with open(".\config.json", mode="r", encoding="utf-8") as f:
        post_data = load(f)
    # api网址
    api_url = 'https://api.lolicon.app/setu/v2'
    # 发送参数并请求色图信息
    response = get(api_url, headers=headers, params=post_data)
    # 将色图信息转为字典
    url_json = response.json()
    # 格式化输出参数
    pprint(post_data)
    # 格式化输出色图信息
    pprint(url_json)
    # 循环读取色图信息
    for info in url_json["data"]:
        # 色图网址
        img_url = info["urls"]["original"]
        # 爬取色图二进制内容
        img_content = get(headers=headers, url=img_url).content
        # 色图pid
        img_pid = info["pid"]
        # 色图后缀名
        img_ext = info["ext"]
        # 以pid作为色图的名字
        with open(f"./temp/{img_pid}.{img_ext}", mode="wb") as f:
            # 保存色图
            f.write(img_content)
        path_list.append(join(getcwd(), f"temp\\{img_pid}.{img_ext}").replace("\\", "/"))
    return path_list


def time_convert(t):
    if t < 60:
        return f"{'%.1f'%t}秒"
    elif t < 3600:
        return f"{int((t % 3600) // 60)}分钟{'%.1f'%(t % 60)}秒"
    else:
        return f"{int(t // 3600)}小时{int((t % 3600) // 60)}分钟{'%.1f'%(t % 60)}秒"


tag = []
parser = argparse.ArgumentParser()
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
