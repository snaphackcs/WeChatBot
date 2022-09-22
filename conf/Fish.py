import random
from json import load
import time


def fish(from_wxid):
    with open("config/info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)
    point = random.randint(1, 99)
    if point <= 9:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了个垃圾。"
    elif point <= 39:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上了一只鲈鱼，也许可以做成吃的？（等待之后物品仓库更新就能加入到物品仓库中了）"
    elif point <= 54:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 钓上来了一只金枪鱼，也许可以做成吃的？（等待之后物品仓库更新就能加入到物品仓库中了）"
    elif point <= 64:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了一个小盒子，里面装满了......社长的女装！"
    elif point <= 79:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了一只琪露诺，把你同化成了笨⑨"
    elif point <= 84:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你居然钓到了社长！非常罕见"
    elif point <= 94:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了一串神秘代码：@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)"
    elif point <= 99:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你调上来了一只韬哥。韬哥向你展示了3张色图，她问你：”你掉的是这个毛玉牛乳老师画的色图，还是这个MANA老师画的色图，还是这个普通的骑兵色图。“你回答：”小孩才选择，大人全都要“。韬哥非常生气，收走了3张色图，抛给你了一个视频，就再也不见了（视频：https://www.bilibili.com/video/BV1vu411R7hs）史称韬哥止导。"
if __name__ == '__main__':
    print(fish("wxid_pdb55y5c8l5n12"))