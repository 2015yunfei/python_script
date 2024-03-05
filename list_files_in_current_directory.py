import os


def list_files(directory):
    """
    列出当前目录下所有文件的名称（包含后缀名）
    """
    file_list = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_list.append(file)
    return file_list


def write_to_file(file_list, output_file):
    """
    将文件名列表写入到输出文件
    """
    with open(output_file, 'w') as f:
        for file_name in file_list:
            f.write(file_name + '\n')


if __name__ == "__main__":
    current_directory = os.getcwd()
    file_list = list_files(current_directory)
    output_file = "output.txt"
    write_to_file(file_list, output_file)
    print(f"All file names have been written to {output_file}.")
