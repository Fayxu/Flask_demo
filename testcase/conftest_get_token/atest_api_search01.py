import pytest
import requests
from commons.requests_util import RequestsUtil


class TestMemGetlist01:

    # 查询会员列表 请求参数1
    params = {
        "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
        "page": "1",
        "perpage": "200",
        "sort_type": "2"
    }

    # 查看会员个人资料 请求数据2
    data = {
        "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
        "uuid": "",
        "token": ""
    }

    # 使用类属性
    @classmethod
    def test_getlist(cls, getlist_url):
        """
        获取会员列表接口02

        :param getlist_url:
        :return:
        """
        # 定义类属性
        params = cls.params
        # print(params)
        # 发送get请求---> 通过session 发送
        getlist_res = RequestsUtil().all_requests('get', url=getlist_url, params=params)
        # 获取 响应结果
        result = getlist_res.json()
        # print(result)
        # 获取结果中的users的 值
        get_users = result['data']['users']  # 字典列表取值：[{a:1},{b:2}] 取key 或者value

        for my_users in get_users:
            # 使用for 循环遍历列表：取出username = "waf123"的字典数据
            if my_users["username"] == "waf123":
                # print(my_users, type(my_users))
                # 取出uuid 的值
                cls.data["uuid"] = my_users["uuid"]
                print(cls.data["uuid"])
        return cls.data["uuid"]

    # 使用类属性
    @classmethod
    def test_getuser_prof(cls, getuser_url, get_token):
        """
        获取会员个人资料03

        :return:
        """
        cls.data["token"] = get_token("access_token")
        data = cls.data
        # 发送post请求---> 通过session 发送
        getuser_profile = RequestsUtil().all_requests('post', url=getuser_url, data=data)
        # 获取响应的格式化json数据
        result = getuser_profile.json()
        print(result)

