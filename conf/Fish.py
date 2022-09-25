import random
from json import load

def fish(from_wxid):
    with open("config/info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)
    with open("config/bao.json", mode="r", encoding="utf-8") as f:
        bao = load(f)
    point = random.randint(1, 100)
    if point <= 40:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了个垃圾。"
    elif point <= 50:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上了一只鲈鱼，也许可以做成吃的？（等待之后物品仓库更新就能加入到物品仓库中了）"
        bao[from_wxid]["fish1"]+=1
    elif point <= 60:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 钓上来了一只金枪鱼，也许可以做成吃的？（等待之后物品仓库更新就能加入到物品仓库中了）"
        bao[from_wxid]["fish2"] += 1
    elif point <= 65:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了一个小盒子，里面装满了......社长的女装！"
        bao[from_wxid]["nvzhuang"] += 1
    elif point <= 75:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了一只琪露诺，把你同化成了笨⑨"
        bao[from_wxid]["qilunuo"] += 1
    elif point <= 85:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你居然钓到了社长！非常罕见"
        bao[from_wxid]["shezhang"] += 1
    elif point <= 90:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来了一串神秘代码：@wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)"
    elif point <= 99:
        return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你调上来了一只韬哥。韬哥向你展示了3张色图，她问你：”你掉的是这个毛玉牛乳老师画的色图，还是这个MANA老师画的色图，还是这个普通的骑兵色图。“你回答：”小孩才选择，大人全都要“。韬哥非常生气，收走了3张色图，抛给你了一个视频，就再也不见了（视频：https://www.bilibili.com/video/BV1vu411R7hs）史称韬哥止导。"

    elif point <= 100:
        yincang=random.randint(0,100)
        if yincang>=99:
            if random.randint(0,1):
                bao[from_wxid]["pink_flower"] += 6
                return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来一个奇怪的小罐子，里面装了一些粉红色的花瓣\n浓郁的香气扑面而来，好像全身上下都温暖了起来。\n收起来吧，似乎在泡茶的时候加入一些能有不错的效果"
            else:
                bao[from_wxid]["blue_flower"] += 6
                return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 你钓上来一个奇怪的小罐子，里面装了一些蓝色的花瓣\n清爽的香气扑面而来，好像头脑立刻就清醒了。\n收起来吧，似乎在泡茶的时候加入一些能有不错的效果"

        elif yincang==1:
            return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 是一套衣服呢，而且还是限定款欸\n快拿去给bot穿上吧。"
        else:
            return f"@{origin[from_wxid]['title']}{origin[from_wxid]['name']} 真可惜，鱼脱勾了\n不过钓鱼佬绝不空军，再试一次吧。"
if __name__ == '__main__':
    print(fish("wxid_pdb55y5c8l5n12"))