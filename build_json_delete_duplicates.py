# 该文件用于在当前目录中构建json文件，并删除构建过程中发现的重复文件
import os
import hashlib
import json

import send2trash


def count_files_in_directory(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count


def remove_empty_dirs(path):
    # 遍历当前目录下的所有文件和文件夹
    for subfolder in os.listdir(path):
        # 构造完整的文件路径
        subfolder_path = os.path.join(path, subfolder)
        # 如果是文件夹，则递归调用
        if os.path.isdir(subfolder_path):
            remove_empty_dirs(subfolder_path)

    # 检查当前目录是否为空
    if not os.listdir(path):
        # 如果为空，则删除该目录
        os.rmdir(path)
        print(f"删除空文件夹: {path}")


def calculate_sha1(file_path):
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()


def get_file_type(file_path):
    return os.path.splitext(file_path)[1]


def recursive_file_list(directory, tot):
    files_json = []
    files_sha1_dict = {}
    number = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            number += 1
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
                print("当前文件：%s  SHA-1：%s" % (file, sha1_value))
            print("%d/%d" % (number, tot))
    return files_json


if __name__ == "__main__":
    # 计算当前文件夹及其子文件夹中的文件数量
    current_directory = '.'  # '.' 表示当前目录
    file_count = count_files_in_directory(current_directory)

    # 递归遍历当前目录，构建字典，并写入json文件
    json_sha1 = recursive_file_list(current_directory, file_count)

    with open('files_sha1.json', 'w') as json_file:
        json.dump(json_sha1, json_file, indent=4)

    remove_empty_dirs(current_directory)

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
