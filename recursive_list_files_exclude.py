import os
import sys


def list_files(directory, excluded_folders=None, output_file=None):
    """
    递归地列出目录下所有文件的名称（包含后缀名），并根据排除列表排除指定文件夹
    """
    file_list = []
    with open(output_file, 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if excluded_folders and any(folder in file_path for folder in excluded_folders):
                    continue
                print(file_path)
                file_list.append(file_path)
        sys.stdout = original_stdout
    return file_list


if __name__ == "__main__":
    current_directory = os.getcwd()
    excluded_folders = [os.path.basename(folder.rstrip("\\")) for folder in sys.argv[1:]]
    output_file = "output.txt"

    file_list = list_files(current_directory, excluded_folders, output_file)
    for file in file_list:
        print(file)

    print("Excluded folders:")
    for folder in excluded_folders:
        if not os.path.isdir(folder):
            print(f"'{folder}' is not a folder in the current directory.")
        else:
            print(f"'{folder}' is a folder in the current directory.")

    with open(output_file, 'a') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        print("Excluded folders:")
        for folder in excluded_folders:
            if not os.path.isdir(folder):
                print(f"'{folder}' is not a folder in the current directory.")
            else:
                print(f"'{folder}' is a folder in the current directory.")
        sys.stdout = original_stdout

    print(f"All file names have been written to {output_file}.")
