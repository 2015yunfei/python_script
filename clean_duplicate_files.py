import os
import send2trash


def find_duplicate_files(directory):
    # 创建一个字典来保存文件大小及其对应的文件名列表
    file_size_dict = {}

    # 遍历当前目录下的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 如果是文件
        if os.path.isfile(file_path):
            # 获取文件大小
            file_size = os.path.getsize(file_path)
            # 将文件大小及其文件名添加到字典中
            if file_size not in file_size_dict:
                file_size_dict[file_size] = [filename]
            else:
                file_size_dict[file_size].append(filename)

    # 遍历字典，对于每个文件大小的列表，如果文件数量大于1，则保留命名较短的文件，将其余文件移动到回收站
    for file_size, filenames in file_size_dict.items():
        if len(filenames) > 1:
            print()
            print(f"以下文件大小为 {file_size} 字节的文件有:")
            for filename in filenames:
                print(filename)
            shortest_filename = min(filenames, key=len)
            for filename in filenames:
                if filename != shortest_filename:
                    file_to_move = os.path.join(directory, filename)
                    print()
                    print(f"Moving {filename} to trash...")
                    print()
                    send2trash.send2trash(file_to_move)


if __name__ == "__main__":
    current_directory = os.getcwd()
    find_duplicate_files(current_directory)
    # 遍历当前目录下的所有子文件夹
    for root, dirs, files in os.walk(current_directory):
        for directory in dirs:
            directory_path = os.path.join(root, directory)
            # 打印当前文件夹路径
            print()
            print("    当前文件夹路径:", directory_path)
            print()
            find_duplicate_files(directory_path)
