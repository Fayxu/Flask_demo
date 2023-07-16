import pytest
import requests
from unit.requests_util import RequestsUtil
from unit.read_yaml import YamlUtil
from unit.get_all_files_path import get_all_files

all_case_files = get_all_files('E:\Mycode\Selflearn_Framework\Flask_demo\data')
case_files2 = all_case_files[2]


class TestMemGetlist02:

    # 查询会员列表 请求参数1
    # params = {
    #     "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
    #     "page": "5",
    #     "perpage": "20",
    #     "sort_type": "2"
    # }

    # 使用参数化，读取用例yaml数据
    @pytest.mark.parametrize("caseinfo", YamlUtil(case_files2).read_case_yaml())
    def test_getlist(self, caseinfo):
        """
        获取会员列表接口02

        :param getlist_url:
        :return:
        """
        # print(caseinfo)

        # 使用读取的yaml用例文件内容 传参
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['url']
        params = caseinfo['requests']['params']

        # 发送get请求---> 通过session 发送
        getlist_res = RequestsUtil().all_requests(method=method, url=url, params=params)
        # 获取 响应结果
        result = getlist_res.json()
        # print(result)
        # 获取结果中的users的 值
        get_users = result['data']['users']  # 字典列表取值：[{a:1},{b:2}] 取key 或者value

        # 找出账号名称是“waf123”的会员信息，先取出含有“waf123”的数据字典
        for my_users in get_users:
            # 使用for 循环遍历列表：取出username = "waf123"的字典数据
            if my_users["username"] == "waf123":
                print(my_users)

                # 取出uuid 的值
                # YamlUtil('./extract.yaml').write_yaml({"uuid": my_users["uuid"]})


# if __name__ == '__main__':
#     pytest.main(['-vs'])
