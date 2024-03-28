"""
腾讯云OCR调用脚本
API文档：https://cloud.tencent.com/document/product/866
产品主页：https://cloud.tencent.com/product/ocr
@author YTSakura
"""
import base64
import json
import urllib
from time import time

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


def tencent_ocr(path, word):
    try:
        word = word
        pic = get_file_content_as_base64(f"{path}")
        cred = credential.Credential("YOUR SECRET ID HERE", "YOUR SECRET KEY HERE")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        req = models.GeneralBasicOCRRequest()
        params = {
            "ImageBase64": f'{pic}'
        }
        req.from_json_string(json.dumps(params))

        resp = client.GeneralBasicOCR(req)
        resp = resp.to_json_string()
        resp = json.loads(resp)
        return resp
        # 如果要输出坐标，请使用下面的代码
        # for detection in resp["TextDetections"]:
        #     if detection["DetectedText"] == f"{word}":
        #         item_polygon = detection["Polygon"]
        #         return (item_polygon[0]['X'], item_polygon[0]['Y'])
        # else:
        #     print("未找到符合条件的文字")

    except TencentCloudSDKException as err:
        print(err)


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
    print(tencent_ocr('PATH', 'WORD'))
