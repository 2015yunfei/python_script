"""
这个脚本的主要功能是比较两个目录中的文件，并将目录B中与目录A中的文件名称或大小匹配的文件移动到回收站。
"""
import os
from send2trash import send2trash


def get_file_size_kb(file_path):
    """返回文件大小，以KB为单位"""
    return os.path.getsize(file_path) // 1024


def hash_directory(directory, hash_table):
    """递归遍历目录，将文件名称和大小存入hash表"""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size_kb = get_file_size_kb(file_path)
            hash_table[file] = file_size_kb


def move_matching_files_to_trash(directory, hash_table):
    """递归遍历目录，将与hash表中匹配的文件移动到回收站"""
    deleted_files_count = 0
    total_deleted_size_kb = 0

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size_kb = get_file_size_kb(file_path)
            if file in hash_table or file_size_kb in hash_table.values():
                print(f"Moving to trash: {file_path}")
                total_deleted_size_kb += file_size_kb
                deleted_files_count += 1
                send2trash(file_path)

    return deleted_files_count, total_deleted_size_kb


def main():
    # 目录A和目录B的路径
    directory_a = "D:\\123\\456"
    directory_b = "D:\\123\\789"

    hash_table = {}

    # 递归遍历目录A，构建hash表
    hash_directory(directory_a, hash_table)

    # 递归遍历目录B，将匹配的文件移动到回收站
    deleted_files_count, total_deleted_size_kb = move_matching_files_to_trash(directory_b, hash_table)

    # 输出移动文件数量和总大小
    print(f"Total files moved to trash: {deleted_files_count}")
    print(f"Total size moved to trash: {total_deleted_size_kb / 1024:.2f} MB")
    print(f"Total size moved to trash: {total_deleted_size_kb / (1024 * 1024):.2f} GB")


if __name__ == "__main__":
    main()
