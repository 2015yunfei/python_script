import os

def copy_and_paste():
    # 获取当前目录
    current_directory = os.getcwd()
    # 读取123.txt文件内容
    with open(os.path.join(current_directory, 'template4HTML.txt'), 'r', encoding='utf-8') as file:
        copied_content = file.read()

    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_directory):
        if filename.endswith('.html'):
            html_file_path = os.path.join(current_directory, filename)
            with open(html_file_path, 'r+', encoding='utf-8') as html_file:
                lines = html_file.readlines()
                for i, line in enumerate(lines):
                    if '</body>' in line:
                        # 在</body>标签后一行插入内容
                        lines.insert(i + 1, copied_content + '\n')
                        break
                # 将修改后的内容写回文件
                html_file.seek(0)
                html_file.truncate()
                html_file.write("".join(lines))

if __name__ == "__main__":
    copy_and_paste()
