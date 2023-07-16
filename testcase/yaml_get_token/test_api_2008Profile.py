import pytest
import requests
from unit.requests_util import RequestsUtil
from unit.read_yaml import YamlUtil
from unit.get_all_files_path import get_all_files

all_case_files = get_all_files('E:\Mycode\Selflearn_Framework\Flask_demo\data')
case_files = all_case_files[1]


class TestMemGetlist02:

    # 查看会员个人资料 请求数据2
    # data = {
    #     "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
    #     "uuid": "",
    #     "token": ""
    # }

    # 使用参数化，读取用例yaml数据
    @pytest.mark.parametrize("caseinfo", YamlUtil(case_files).read_case_yaml())
    def test_getuser_prof(self, caseinfo):
        """
        获取会员个人资料03

        :return:
        """

        # 通过读取yaml文件, 将中间变量 access_token/uuid 从字典中获取
        caseinfo['requests']['data']['uuid'] = YamlUtil('./extract.yaml').read_yaml().get("uuid")
        caseinfo['requests']['data']['token'] = YamlUtil('./extract.yaml').read_yaml().get("access_token")

        # 使用读取的yaml用例文件内容 传参
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['url']
        data = caseinfo['requests']['data']

        # 发送post请求---> 通过session 发送
        getus_prof_res = RequestsUtil().all_requests(method=method, url=url, data=data)
        # 获取响应的格式化json数据
        result = getus_prof_res.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs'])
