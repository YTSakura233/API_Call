"""
阿里云OCR调用脚本
API文档：https://help.aliyun.com/document_detail/295338.html
产品文档：https://ai.aliyun.com/ocr/general
@author YTSakura
"""
import json
from time import time

from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_util import models as util_models

ALIBABA_CLOUD_ACCESS_KEY_ID = 'YOUR ACCESS KEY ID HERE'
ALIBABA_CLOUD_ACCESS_KEY_SECRET = 'YOUR ACCESS KEY SECRET HERE'

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> OpenApiClient:
        config = open_api_models.Config(
            access_key_id=ALIBABA_CLOUD_ACCESS_KEY_ID,
            access_key_secret=ALIBABA_CLOUD_ACCESS_KEY_SECRET
        )
        config.endpoint = 'ocr-api.cn-hangzhou.aliyuncs.com'
        return OpenApiClient(config)

    @staticmethod
    def create_api_info() -> open_api_models.Params:
        """
        API 相关
        @param path: params
        @return: OpenApi.Params
        """
        params = open_api_models.Params(
            # 接口名称,
            action='RecognizeGeneral',
            # 接口版本,
            version='2021-07-07',
            # 接口协议,
            protocol='HTTPS',
            # 接口 HTTP 方法,
            method='POST',
            auth_type='AK',
            style='V3',
            # 接口 PATH,
            pathname=f'/',
            # 接口请求体内容格式,
            req_body_type='json',
            # 接口响应体内容格式,
            body_type='json'
        )
        return params

    @staticmethod
    def main(path, word) -> None:
        word = word
        client = Sample.create_client()
        params = Sample.create_api_info()
        body = StreamClient.read_from_file_path(f'{path}')
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest(
            stream=body
        )
        resp = client.call_api(params, request, runtime)
        print(resp)
        # 如果需要输出坐标，则使用下方的代码
        # data = json.loads(resp['body']['Data'])
        # for word_info in data["prism_wordsInfo"]:
        #     if word_info["word"] == f"{word}":
        #         item_polygon = word_info["pos"][0]
        #         print((item_polygon['x'], item_polygon['y']))
        #         break
        # else:
        #     print("未找到指定的文本")


if __name__ == '__main__':
    Sample.main('PATH', 'WORD')
