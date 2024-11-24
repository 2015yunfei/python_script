# 该文件用于在当前目录中构建json文件，并删除构建过程中发现的重复文件
import os
import hashlib
import json

import send2trash


def calculate_sha1(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()


def get_file_type(file_path):
    return os.path.splitext(file_path)[1]


def recursive_file_list(directory):
    files_json = []
    files_sha1_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            sha1_value = calculate_sha1(file_path)
            file_type = get_file_type(file)
            if sha1_value in files_sha1_dict:
                # 将该文件移动到回收站
                send2trash.send2trash(file_path)
                print("\n当前文件：%s\n和文件：%s\nSHA-1值发生冲突\n已经将当前文件：%s移动到回收站\n" % (
                    file, files_sha1_dict[sha1_value]["file_name"], file))
            else:
                # 使用SHA-1值作为键，文件名称和文件类型作为值
                files_sha1_dict[sha1_value] = {
                    "file_name": file,
                    "file_type": file_type
                }
                files_json.append({
                    "file_name": file,
                    "file_type": file_type,
                    "sha1": sha1_value
                })
    return files_json


if __name__ == "__main__":
    # 递归遍历当前目录，构建字典，并写入json文件
    current_directory = '.'  # '.' 表示当前目录
    json_sha1 = recursive_file_list(current_directory)

    with open('files_sha1.json', 'w') as json_file:
        json.dump(json_sha1, json_file, indent=4)

# import os
# import hashlib
# import json
#
# import send2trash
#
#
# def calculate_sha1(file_path):
#     sha1_hash = hashlib.sha1()
#     with open(file_path, "rb") as f:
#         # Read and update hash in chunks of 4K
#         for byte_block in iter(lambda: f.read(4096), b""):
#             sha1_hash.update(byte_block)
#     return sha1_hash.hexdigest()
#
#
# def get_file_type(file_path):
#     return os.path.splitext(file_path)[1]
#
#
# def recursive_file_list(directory):
#     files_json = []
#     files_sha1_dict = {}
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             sha1_value = calculate_sha1(file_path)
#             file_type = get_file_type(file)
#             if sha1_value in files_sha1_dict:
#                 # 将该文件移动到回收站
#                 send2trash.send2trash(file_path)
#                 print("当前文件：%s\n和文件：%s\nSHA-1值发生冲突\n已经将当前文件：%s移动到回收站" % (
#                     file, files_sha1_dict[sha1_value]["file_name"], file))
#             else:
#                 # 使用SHA-1值作为键，文件名称和文件类型作为值
#                 files_sha1_dict[sha1_value] = {
#                     "file_name": file,
#                     "file_type": file_type
#                 }
#                 files_json.append({
#                     "file_name": file,
#                     "file_type": file_type,
#                     "sha1": sha1_value
#                 })
#     return files_json, files_sha1_dict
#
#
# def build_sha1_dict_from_json(file_path):
#     # 初始化一个空字典来存储结果
#     files_sha1_dict = {}
#
#     # 读取JSON文件
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#
#         # 遍历文件中的每个项目，并构建字典
#         for item in data:
#             sha1_value = item['sha1']
#             files_sha1_dict[sha1_value] = {
#                 "file_name": item['file_name'],
#                 "file_type": item['file_type']
#             }
#
#     return files_sha1_dict
#
#
# if __name__ == "__main__":
#     # 检查当前目录下是否存在名为 "files_sha1.json" 的文件
#     file_path = "files_sha1.json"
#     if os.path.exists(file_path):
#         # 根据存在的json文件构建字典
#         print("当前目录中存在文件 'files_sha1.json'")
#         dict_sha1 = build_sha1_dict_from_json(file_path)
#     else:
#         # 递归遍历当前目录，构建字典，并写入json文件
#         print("文件 'files_sha1.json' 不存在于当前目录下。")
#
#         current_directory = '.'  # '.' 表示当前目录
#         json_sha1, dict_sha1 = recursive_file_list(current_directory)
#
#         with open('files_sha1.json', 'w') as json_file:
#             json.dump(json_sha1, json_file, indent=4)
