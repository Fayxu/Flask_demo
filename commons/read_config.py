# 读取common 文件下的 config.yaml 文件内容
import json
import yaml
from unit.get_all_files_path import get_all_files


# 获取data 下的所以yaml文件
all_case_files = get_all_files('E:\Mycode\Selflearn_Framework\Flask_demo\data')
# print(all_case_files)
case_files = all_case_files[0]


def replace_method(**kwargs):
    with open(case_files, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 序列化
    data1 = json.dumps(data)
    print(data1)

    # for key, value in kwargs.items():
    #     data1 = data1.replace(f'${{{key}}}', value)
    #
    # # 反序列化
    # data2 = json.loads(data1)
    #
    # return data2


print(replace_method())
# print(replace_method(host='http://hn216.api.yesapi.cn/api/App/User'))
