import pytest
import logging
from commons.requests_util import RequestsUtil


class TestMemLogin01:

    # 登录接口，请求数据1
    data = {
        "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
        "username": "waf123",
        "password": "e10adc3949ba59abbe56e057f20f883e"
    }


    # 使用类属性
    @classmethod
    def test_login(cls, login_url, set_token):
        """
        登录接口01

        :param login_url:
        :return:
        """
        # 调用类属性
        # url = login_url
        data = cls.data
        # 发送post请求 ---> 通过session 发送
        login_res = RequestsUtil().all_requests('post', url=login_url, data=data)

        result = login_res.json()  # 返回的数据是： dict = {a:{b:1}}字典嵌套字典，取值：dict['a']['b'] 或者 dict.get().get()
        # print(result, type(result))
        # cls.access_token = result['data']['token']
        access_token = result['data']['token']
        set_token("access_token", access_token)

