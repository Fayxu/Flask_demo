# -*- coding: utf-8 -*-
"""

"""
import os


def get_all_files(file_path, yaml_data_switch=True) -> list:
    """
    获取文件路径
    :param file_path: 目录路径
    :param yaml_data_switch: 是否过滤文件为 yaml格式， True则过滤
    :return:
    """
    filename_path = []

    # 获取所有文件下的子文件名称
    for root, dirs, files in os.walk(file_path):
        for _file_path in files:
            path = os.path.join(root, _file_path)
            if yaml_data_switch:
                if 'yaml' in path or '.yml' in path:
                    filename_path.append(path)
            else:
                filename_path.append(path)
    return filename_path


# def get_all_filenames(filename_path):
#
#     filenames = []
#     for filename in filename_path:
#         if 'yaml' in filename or '.yml' in filename:
#             filename = filename.split('\\')[-1]
#             filenames.append(filename)
#
#     return filenames
#
#
# a = ['..\\data\\2003_Mem_Login.yaml', '..\\data\\2008_Mem_UserProfile.yaml', '..\\data\\2013_Mem_GetList.yaml']
#
#
# print(get_all_files('..\\data'))
# print(get_all_filenames(a))
