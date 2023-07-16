# 统一接口请求封装
import requests


class RequestsUtil:
    """
    使用session 进行请求的思想，设计参数： method, url, **kwargs
    只需传入方法，和地址，其他参数走不定参数
    """
    sess = requests.Session()
    def all_requests(self, method, url, **kwargs):
        ress = RequestsUtil.sess.request(method, url, **kwargs)
        return ress