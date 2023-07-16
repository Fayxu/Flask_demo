import pytest
from unit.requests_util import RequestsUtil
from unit.read_yaml import YamlUtil
from unit.get_all_files_path import get_all_files


# 获取data 下的所以yaml文件
all_case_files = get_all_files('E:\Mycode\Selflearn_Framework\Flask_demo\data')
# print(all_case_files)
case_files = all_case_files[0]
# case_files = str([case[0] for case in all_case_files if '2003_Mem_Login.yaml' in case])
# print(case_files)


class TestMemLogin02:

    # 登录接口，请求数据1
    # login_url = 'http://hn216.api.yesapi.cn/api/App/User/Login'
    # data = {
    #     "app_key": "0DF5B8C9BE5133A6C86CC4A024D03A98",
    #     "username": "waf123",
    #     "password": "e10adc3949ba59abbe56e057f20f883e"
    # }

    # 使用参数化，读取用例yaml数据
    @pytest.mark.parametrize("caseinfo", YamlUtil(case_files).read_case_yaml())
    def test_login(self, caseinfo):
        """
        登录接口01
        login_url: 记录到 yaml用例中
        :param
        :return:
        """

        # 使用读取的yaml用例文件内容 传参
        method = caseinfo['requests']['method']
        url = caseinfo['requests']['host'] + caseinfo['requests']['url']
        print(url)
        data = caseinfo['requests']['data']

        # 发送post请求 ---> 通过session 发送
        login_res = RequestsUtil().all_requests(method=method, url=url, data=data)

        result = login_res.json()  # 返回的数据是： dict = {a:{b:1}}字典嵌套字典，取值：dict['a']['b'] 或者 dict.get().get()
        print(result, type(result))

        # 通过写入yaml文件, 将中间变量 access_token, uuid 写入extract.yaml 文件
        YamlUtil('./extract.yaml').write_yaml({"access_token": result['data']['token']})
        YamlUtil('./extract.yaml').write_yaml({"uuid": result['data']['uuid']})

        # 断言
        if result['data']['err_code'] == 0:
            print('登录成功')
        elif result['data']['err_code'] == 1:
            # 1登录失败，密码错误；
            print(result['data']['err_msg'])
        elif result['data']['err_code'] == 2:
            # 2登录失败，密码错误
            print(result['data']['err_msg'])
        elif result['data']['err_code'] == 3:
            # 3会员已过期，请联系管理员或开发者
            print(result['data']['err_msg'])
        else:
            # 4账号已被封号
            print(result['data']['err_msg'])


if __name__ == '__main__':
    pytest.main(['-vs'])
