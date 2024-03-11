import os
import shutil


def move_files_up():
    # 获取当前目录
    current_directory = os.getcwd()

    # 遍历当前目录下的所有文件和文件夹
    for root, dirs, files in os.walk(current_directory):
        # 如果当前目录不是根目录，则将文件移动到上一级目录
        if root != current_directory:
            for file in files:
                # 构建源文件路径和目标文件路径
                source_file = os.path.join(root, file)
                destination_file = os.path.join(current_directory, file)

                # 移动文件
                shutil.move(source_file, destination_file)
                print(f"Moved {source_file} to {destination_file}")


if __name__ == "__main__":
    move_files_up()
