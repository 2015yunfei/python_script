# 该文件利用当前目录中的json文件构建一个字典，然后遍历当前目录，删除字典中存在的重复项

import os
import hashlib
import json

import send2trash


def build_sha1_dict_from_json(file_path):
    # 初始化一个空字典来存储结果
    files_sha1_dict = {}

    # 读取JSON文件
    with open(file_path, 'r') as file:
        data = json.load(file)

        # 遍历文件中的每个项目，并构建字典
        for item in data:
            sha1_value = item['sha1']
            files_sha1_dict[sha1_value] = {
                "file_name": item['file_name'],
                "file_type": item['file_type']
            }

    return files_sha1_dict


def calculate_sha1(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()


def recursive_delete_files(dict_sha1, current_directory):
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            file_path = os.path.join(root, file)
            sha1_value = calculate_sha1(file_path)
            if sha1_value in dict_sha1:
                # 将该文件移动到回收站
                send2trash.send2trash(file_path)
                print("当前文件：%s\n和文件：%s\nSHA-1值发生冲突\n已经将当前文件：%s移动到回收站" % (
                    file, dict_sha1[sha1_value]["file_name"], file))


if __name__ == "__main__":
    # 检查当前目录下是否存在名为 "files_sha1.json" 的文件
    file_path = "files_sha1.json"
    if os.path.exists(file_path):
        # 根据存在的json文件构建字典
        print("当前目录中存在文件 'files_sha1.json'")
        dict_sha1 = build_sha1_dict_from_json(file_path)

        current_directory = '.'  # '.' 表示当前目录
        recursive_delete_files(dict_sha1, current_directory)
    else:
        # 递归遍历当前目录，构建字典，并写入json文件
        print("文件 'files_sha1.json' 不存在于当前目录下。\n记得先运行另外一个脚本得到json文件之后再运行此脚本")
