"""
阿里云-通义千问VL模型
@author YTSakura
"""
from http import HTTPStatus
from time import time

import dashscope


def get_value(path, question):
    dashscope.api_key = "YOUR API KEY HERE"  # 请替换这里的apikey
    messages = [{
            "role": "user",
            "content": [
                {"image": rf"{path}"},
                {"text": f"{question}"}
            ]
        }
    ]
    # qwen-vl-max or qwen-vl-plus
    response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                     messages=messages,
                                                     seed=6324)
    if response.status_code == HTTPStatus.OK:
        resp = response.output.choices[0].message.content[0].get('text')
        print(resp)
    else:
        print(response.code)
        print(response.message)


if __name__ == '__main__':
    get_value(r"file://PATH", "QUESTION")
