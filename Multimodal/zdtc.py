"""
紫东太初调用接口（图片被莫名其妙和谐导致接口无法调用，故弃用）
@author YTSakura
"""
import base64
import urllib

import requests


def get_value(question, base):
    params = {
        'picture': f'{base}',
        'question': f'{question}',
        'model_code': 'taichu_vqa_10b',
        'api_key': 'YOUR API KEY HERE',
        'repetition_penalty': 2.0,
    }
    url = 'https://ai-maas.wair.ac.cn/maas/v1/model_api/invoke'
    response = requests.post(url, json=params)
    if response.status_code == 200:
        if response.json()['code'] == 0:
            return response.json()['data']['content']
        else:
            return response.json()['msg']
    else:
        print('filed')


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


if __name__ == '__main__':
    base = get_file_content_as_base64('PATH')  # 请更改图片地址
    question = "QUESTION"  # 请更改question信息
    value = get_value(question, base)
    print(value)
