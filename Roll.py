import random


def roll(args):
    points = sum(random.randint(1, args["dice"]) for _ in range(args["num"]))
    with open("temp.txt", mode="w") as doc:
        doc.write(f"投了{args['num']}个d{args['dice']}，结果是{points}")



