import random
from json import load, dump


def chag(args):
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)
    with open("temp.json", mode="w") as doc:
    origin[doc["wxid"]]["score"] = args["point"]
    origin[doc["wxid"]]["sign_days"] = args["day"]
    with open("info.json", mode="w") as f:
        dump(origin, f, indent=4)