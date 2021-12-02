import json
import numpy as np


def json2dict(direct_path: str):
    with open(direct_path, encoding="utf8") as json_file:
        data = json.load(json_file)
    return data

def dat2numpy(direct_path: str):
    sed = np.loadtxt(direct_path, unpack = True)
    return sed