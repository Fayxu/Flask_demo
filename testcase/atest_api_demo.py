import pytest
import requests
# from pkg_resources import iter_entry_points
"""
自己写了3个接口，查看需要封装哪些东西？
1.请求方法重复调用
2.请求参数参数化，暂时未使用
3.请求有接口依赖，如何做比较方便？
4.请求参数中有固定数据，是否放全局配置文件方便？
5.没有增加断言 和数据库查询
6.日志查看不清晰
7.测试数据和测试用例放到一起，不方便维护
8.没有使用测试报告；

"""


class TestMemGetlist:
    # 登录接口地址
    # login_url = 'http://hn216.api.yesapi.cn/api/App/User/Login'

    # 查询接口地址
    # getlist_url = 'http://hn216.api.yesapi.cn/api/App/User/GetList'

    # 登录接口，请求数据1
    data1 = {
        "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
        "username": "waf123",
        "password": "e10adc3949ba59abbe56e057f20f883e"
    }

    # 查询参数
    params = {
        "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
        "token": "",
        "page": "1",
        "perpage": "200",
        "sort_type": "2"
    }

    # 查看会员个人资料 请求数据2
    data2 = {
        "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
        "uuid": "",
        "token": ""

    }

    # 使用类属性
    @classmethod
    def test_login(cls, login_url):
        """
        登录接口

        :param login_url:
        :return:
        """
        # 调用类属性
        # url = login_url
        data = cls.data1
        # 发送post请求
        login_res = requests.post(url=login_url, data=data)
        result = login_res.json()  # 返回的数据是： dict = {a:{b:1}}字典嵌套字典，取值：dict['a']['b'] 或者 dict.get().get()
        # print(result, type(result))
        access_token1 = result['data']['token']
        # access_token2 = result.get('data').get('token')
        # print(access_token1)
        cls.params['token'] = access_token1
        # print(cls.params['token'])
        # print(cls.params)
        return cls.params['token']

    # 使用类属性
    @classmethod
    def test_getlist(cls, getlist_url):
        """
        获取会员列表接口

        :param getlist_url:
        :return:
        """
        # 调用类属性
        # url = getlist_url
        params = cls.params
        # print(params)
        getlist_res = requests.get(url=getlist_url, params=params)
        result = getlist_res.json()
        # print(result)
        getuser = result['data']['users']  # 字典列表取值：[{a:1},{b:2}] 取key 或者value

        for my_users in getuser:
            # 使用for 循环遍历列表：取出username = "waf123"的字典数据
            if my_users["username"] == "waf123":
                # print(my_users, type(my_users))
                uuid = my_users['uuid']
                cls.data2['uuid'] = uuid
                # print(cls.data2['uuid'])

        # my_users = [my_users for my_users in getuser if my_users['username'] == 'waf123']  # 另外的方法：取出单个字典列表
        # uuid = my_users[0]['uuid']
        # print(uuid)

        # print(cls.data2['uuid'])
        return cls.data2['uuid']

    # 使用类属性
    @classmethod
    def test_getuser_prof(cls, getuser_url):
        """
        获取会员个人资料

        :return:
        """
        data = cls.data2
        cls.data2['token'] = cls.params['token']
        getuser_profile = requests.post(url=getuser_url, data=data)
        result = getuser_profile.json()
        # print(result)


if __name__ == '__main__':
    pytest.main()

