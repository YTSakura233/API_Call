"""
网易有道OCR调用脚本
API文档：https://ai.youdao.com/DOCSIRMA/html/ocr/api/tyocr/index.html
产品主页：https://ai.youdao.com/product-ocr-print.s
@author YTSakura
"""
import base64
import json
from time import time

import requests

from utils.AuthV3Util import addAuthParams

# 您的应用ID
APP_KEY = 'YOUR APP KEY HERE'
# 您的应用密钥
APP_SECRET = 'YOUR APP SECRET HERE'


def createRequest(path, word):
    word = word

    lang_type = 'zh-CHS'
    detect_type = '10012'
    doc_type = 'json'
    image_type = '1'

    # 数据的base64编码
    img = readFileAsBase64(path)
    data = {'img': img, 'langType': lang_type, 'detectType': detect_type, 'docType': doc_type, 'imageType': image_type}

    addAuthParams(APP_KEY, APP_SECRET, data)

    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = doCall('https://openapi.youdao.com/ocrapi', header, data, 'post')
    data = json.loads(res.content)
    print(data)
    # 如果需要输出坐标，请使用下面的代码
    # for region in data['Result']['regions']:
    #     for line in region['lines']:
    #         if line['text'] == f'{word}':
    #             print((int(line['boundingBox'].split(',')[0]), int(line['boundingBox'].split(',')[1])))

def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)


def readFileAsBase64(path):
    f = open(path, 'rb')
    data = f.read()
    return str(base64.b64encode(data), 'utf-8')


if __name__ == '__main__':
    createRequest('PATH', 'WORD')
