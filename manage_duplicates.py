"""
遍历指定目录及其子目录下的所有文件，并根据文件名或文件大小删除重复的文件
"""
import os
import sys
from send2trash import send2trash
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

# Add logging to a file
file_handler = logging.FileHandler('output.txt')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(file_handler)

total_size_moved = 0  # Global variable to track total size moved to recycle bin


def move_to_recycle_bin(file_path, reason):
    global total_size_moved
    file_size = os.path.getsize(file_path)  # size in GB
    total_size_moved += file_size
    message = f'{reason}--Moving {file_path} to recycle bin'
    logger.info(message)
    send2trash(file_path)


def traverse_directory(root_dir, file_info):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path) / 1024  # size in KB
            if filename in file_info:
                move_to_recycle_bin(file_path, 'Duplicate file name')
            elif file_size in file_info.values():
                move_to_recycle_bin(file_path, 'Duplicate file size')
            else:
                file_info[filename] = file_size


def remove_empty_dirs(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            if not os.listdir(dir_full_path):  # Check if the directory is empty
                os.rmdir(dir_full_path)
                message = f'Removed empty directory: {dir_full_path}'
                logger.info(message)


def main():
    global total_size_moved
    args = sys.argv[1:]
    file_info = {}

    if not args or args[0] == '-r':
        root_dir = os.getcwd()
    else:
        root_dir = args[0]

    traverse_directory(root_dir, file_info)
    remove_empty_dirs(root_dir)

    message = f'Total size moved to recycle bin: {total_size_moved / (1024 * 1024 * 1024): .6f} GB'
    logger.info(message)


if __name__ == '__main__':
    main()
