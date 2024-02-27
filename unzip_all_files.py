import os
import zipfile
import rarfile


def extract_files_in_directory(directory):
    # 获取当前目录下的所有文件
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)
        if zipfile.is_zipfile(file_path):
            # 如果是zip文件，解压缩
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(directory)
            print(f"解压缩 {file} 完成")
        elif rarfile.is_rarfile(file_path):
            # 如果是rar文件，解压缩
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(directory)
            print(f"解压缩 {file} 完成")
        else:
            print(f"文件 {file} 不是压缩文件，跳过")


if __name__ == "__main__":
    current_directory = os.getcwd()
    extract_files_in_directory(current_directory)
