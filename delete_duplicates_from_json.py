# 该文件利用当前目录中的json文件构建一个字典，然后遍历当前目录，删除字典中存在的重复项

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


def recursive_delete_files(dict_sha1, current_directory, tot):
    number = 0
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            number += 1
            file_path = os.path.join(root, file)
            sha1_value = calculate_sha1(file_path)
            if sha1_value in dict_sha1:
                # 将该文件移动到回收站
                send2trash.send2trash(file_path)
                print("当前文件：%s\n和文件：%s\nSHA-1值发生冲突\n已经将当前文件：%s移动到回收站" % (
                    file, dict_sha1[sha1_value]["file_name"], file))
            else:
                print("当前文件：%s  SHA-1：%s" % (file, sha1_value))
            print("%d/%d" % (number, tot))


if __name__ == "__main__":
    # 计算当前文件夹及其子文件夹中的文件数量
    current_directory = '.'
    file_count = count_files_in_directory(current_directory)

    # 检查当前目录下是否存在名为 "files_sha1.json" 的文件
    file_path = "files_sha1.json"
    if os.path.exists(file_path):
        # 根据存在的json文件构建字典
        print("当前目录中存在文件 'files_sha1.json'")
        dict_sha1 = build_sha1_dict_from_json(file_path)

        current_directory = '.'  # '.' 表示当前目录
        recursive_delete_files(dict_sha1, current_directory, file_count)
        remove_empty_dirs(current_directory)
    else:
        # 递归遍历当前目录，构建字典，并写入json文件
        print("文件 'files_sha1.json' 不存在于当前目录下。\n记得先运行另外一个脚本得到json文件之后再运行此脚本")
