"""
百度图像识别API
@author YTSakura
"""
import base64
import urllib
from time import sleep

import requests
import json

API_KEY = "YOUR API KEY HERE"
SECRET_KEY = "YOUR SECRET KEY HERE"


def get_result_id(path, question):
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/request?access_token=" + get_access_token()
    base = get_file_content_as_base64(path, False)
    payload = json.dumps({
        "image": f"{base}",
        "question": f"{question}"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    result_id = response.json()['result']['task_id']
    print(result_id)
    return result_id


def get_result(result_id):
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image-understanding/get-result?access_token=" + get_access_token()

    payload = json.dumps({
        "task_id": f"{result_id}"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.json()['result']['description']
    return result


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    result_id = get_result_id("PATH", "QUESTION")
    sleep(20)
    result = get_result(result_id)
    print(result)

