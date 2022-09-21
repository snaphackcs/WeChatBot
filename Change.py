import random
from json import load, dump


def chag(args):
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = load(f)
    origin[args["user"]]["score"] = args["point"]
    origin[args["user"]]["sign_days"] = args["day"]
    with open("info.json", mode="w") as f:
        dump(origin, f, indent=4)