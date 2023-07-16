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


# -------------------------------f------------------------------

# 设置全局 token
global_token = {}


# 设置token
@pytest.fixture
def set_token():
    """

    设置全局变量access_token，用于关联接口依赖参数
    :return:
    """
    # pass
    def _set_token(k, v):
        global_token[k] = v

    return _set_token


# 获取及传递token
@pytest.fixture(scope="class")
def get_token():
    """

    从 access_token 中取值
    :return:
    """
    def _get_token(k):
        return global_token.get(k)
    return _get_token
