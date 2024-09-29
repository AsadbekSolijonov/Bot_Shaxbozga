import json

from run import BASE_DIR


def read(lang):
    with open(f"{BASE_DIR}/locale/{lang}/messages.json") as file:
        datas = json.load(file)
        return datas
