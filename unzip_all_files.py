import os
import zipfile
import rarfile
import send2trash

def extract_files_in_directory(directory):
    # 获取当前目录下的所有文件
    files = os.listdir(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        if zipfile.is_zipfile(file_path):
            # 如果是zip文件，解压缩
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                try:
                    zip_ref.extractall(directory)
                    print(f"解压缩 {file} 完成")
                    send2trash.send2trash(file_path)  # 将文件移动到回收站
                    print(f"已将 {file} 移动到回收站")
                except RuntimeError:
                    print(f"文件 {file} 需要密码，跳过解压")
        elif rarfile.is_rarfile(file_path):
            # 如果是rar文件，解压缩
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                try:
                    rar_ref.extractall(directory)
                    print(f"解压缩 {file} 完成")
                    send2trash.send2trash(file_path)  # 将文件移动到回收站
                    print(f"已将 {file} 移动到回收站")
                except rarfile.PasswordRequired:
                    print(f"文件 {file} 需要密码，跳过解压")
        else:
            print(f"文件 {file} 不是压缩文件，跳过")

if __name__ == "__main__":
    current_directory = os.getcwd()
    extract_files_in_directory(current_directory)
