"""
本模块介绍 【正则表达式】的封装方法

首先需要导入包
import re

使用的方法是：

re.match()   用于从字符串的开始处进行匹配，如果在起始位置匹配成功，则返回 Match 对象，否则返回 None
re.search()  在整个字符串中搜索第一个匹配的值，如果匹配成功，则返回 Match 对象，否则返回 None
re.findall() 在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回所有符合条件的结果;如果匹配不成功，返回空列表。


"""
import re
str = {'ret': 200, 'data': {'err_code': 0, 'err_msg': '',
                            'info': {'uuid': '14A292E325FCE0E21DB74F7E54DADBD8',
                                     'username': 'waf123',
                                     'role': 'user',
                                     'rolename': '普通会员',
                                     'register_time': '2023-06-27 21:29:20',
                                     'register_ip': '117.143.155.118',
                                     'status': 0}},
       'msg': '', '_t': 1688025219, '_auth': 'bc698350f82eaed4613ba7906fbd2420'}

# re.search("uudi:str", str)