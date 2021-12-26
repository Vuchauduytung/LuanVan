import io
import json
import base64
import numpy as np
from typing import Union
import PIL.Image as Image
from PIL.ImageQt import ImageQt


def json2dict(direct_path: str):
    with open(direct_path, encoding="utf8") as json_file:
        data = json.load(json_file)
    return data

def dict2json(target_path: str, data: Union[list, dict]):
    with open(target_path, 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4)

def dat2numpy(direct_path: str):
    sed = np.loadtxt(direct_path, unpack = True)
    return sed

def img2str(direct_path: str):
    with open(direct_path, mode='rb') as file:
        img = file.read()
    str_code = base64.b64encode(img).decode('utf-8')
    return str_code

def decode_img(code: str):
    byte = base64.b64decode(code)
    img = Image.open(io.BytesIO(byte))
    image_qt = ImageQt(img)
    return image_qt