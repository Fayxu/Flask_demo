import pytest
from unit.read_yaml import YamlUtil


# 1.添加装饰器，使用前置获取登录url
# @pytest.fixture(scope='function', name='login_url')
# def login_url():
#     login_url = 'http://hn216.api.yesapi.cn/api/App/User/Login'
#     yield login_url


# 添加装饰器，使用前置：获取会员列表url
# @pytest.fixture(scope='function', name='getlist_url')
# def get_memlist_url():
#     getlist_url = 'http://hn216.api.yesapi.cn/api/App/User/GetList'
#     yield getlist_url


# 添加装饰器，使用前置：获取会员个人资料url
# @pytest.fixture(scope='function', name='getuser_url')
# def get_userpro_url():
#     getuser_url = 'http://hn216.api.yesapi.cn/api/App/User/Profile'
#     yield getuser_url


# 2.清除装饰器，使用前置：在使用变量之前先清除 extract.yaml 文件内容
@pytest.fixture(scope='session', autouse=True)
def clear_token():
    YamlUtil('./extract.yaml').clear_yaml()


# 2.1清除装饰器，使用后置：范围为：session，在使用变量之后再清除 extract.yaml 文件内容
# 需要开启自动使用 (需要再调试，后置有问题)
# @pytest.fixture(scope='session', autouse=True)
# def clear_token():
#     pass
#     yield YamlUtil('./extract.yaml').clear_yaml()
