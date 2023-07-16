# 读取yaml文件保存的中间变量
import os

import yaml


class YamlUtil:

    def __init__(self, yaml_file):

        self.yaml_file = yaml_file

    # 读取yaml文件内容 (中间变量/)
    def read_yaml(self):
        #  yaml.load ：加载文件
        with open(self.yaml_file, encoding='utf-8')as f:
            results = yaml.load(stream=f, Loader=yaml.FullLoader)
            return results

    # 写入yaml文件内容 (中间变量)
    def write_yaml(self, data):
        # 使用不同模式写入: w, 覆盖写入； a, 增加写入
        # yaml.dump ：写入文件
        with open(self.yaml_file, encoding='utf-8', mode='a')as f:
            yaml.dump(data, stream=f, allow_unicode=True)

        # pass

    # 清除yaml文件内容 (中间变量)
    def clear_yaml(self):
        # pass
        # f.truncate() 清空文件
        with open(self.yaml_file, encoding='utf-8', mode='w')as f:
            f.truncate()

    # 读取 yaml用例数据
    def read_case_yaml(self):
        with open(self.yaml_file, encoding='utf-8')as f:
            results = yaml.load(stream=f, Loader=yaml.FullLoader)
            return results


# if __name__ == '__main__':
    # 读文件内容调用
    # a = YamlUtil(os.getcwd() + '/extract.yaml').read_yaml()
    # print(a)
    # 增加内容调用
    # YamlUtil(os.getcwd() + '/extract.yaml').write_yaml({"sex": "male",
    #                                                     "name": "jack",
    #                                                     "age": 20
    #                                                     })
    # 清空内容调用
    # YamlUtil(os.getcwd() + '/extract.yaml').clear_yaml()

