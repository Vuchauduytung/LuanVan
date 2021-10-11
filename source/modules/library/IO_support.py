import json


def json2dict(direct_path: str) -> dict:
    with open(direct_path, encoding="utf8") as json_file:
        data = json.load(json_file)
    return data

