import random
from json import dump


def roll(args):
    points = sum(random.randint(1, args["dice"]) for _ in range(args["num"]))
    with open("temp.json", mode="w") as doc:
        dump({"text": f"投了{args['num']}个d{args['dice']}，结果是{points}"}, doc, indent=4)
