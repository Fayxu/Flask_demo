import pytest


# 添加装饰器，使用前置获取登录url
@pytest.fixture(scope='function', name='login_url')
def login_url():
    # pass
    login_url = 'http://hn216.api.yesapi.cn/api/App/User/Login'
    yield login_url


# 添加装饰器，使用前置：获取会员列表url
@pytest.fixture(scope='function', name='getlist_url')
def get_memlist_url():
    # pass
    getlist_url = 'http://hn216.api.yesapi.cn/api/App/User/GetList'
    yield getlist_url


# 添加装饰器，使用前置：获取会员列表url
@pytest.fixture(scope='function', name='getuser_url')
def get_userpro_url():
    # pass
    getuser_url = 'http://hn216.api.yesapi.cn/api/App/User/Profile'
    yield getuser_url
