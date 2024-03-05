import os


def list_files(directory):
    """
    递归地列出目录下所有文件的名称（包含后缀名）
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), directory))
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
