"""
阿里云-通义千问VL模型
@author YTSakura
"""
from http import HTTPStatus

import dashscope


def simple_multimodal_conversation_call(path, question):
    dashscope.api_key = "YOUR API KEY HERE"  # 请替换这里的apikey
    messages = [
        {
            "role": "user",
            "content": [
                {"image": rf"{path}"},
                {"text": f"{question}"}
            ]
        }
    ]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-max',
                                                     messages=messages)
    if response.status_code == HTTPStatus.OK:
        print(response.output.choices[0].message.content[0].get('text'))
        return response.output.choices[0].message.content[0].get('text')
    else:
        print(response.code)
        print(response.message)
