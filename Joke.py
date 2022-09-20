

import json
import random

def joke(from_wxid):
    with open("info.json", mode="r", encoding="utf-8") as f:
        origin = json.load(f)
    with open("config/jokes.json", "r", encoding="utf-8") as fp:
        jokes = json.load(fp)
    jokes = jokes["jokes"]
    idx = random.randint(0, len(jokes)-1)
    return f"@{origin[from_wxid]['name']} [{origin[from_wxid]['title']}]\n{jokes[idx]}"

if __name__ == "__main__":
    print(joke("wxid_pdb55y5c8l5n12"))