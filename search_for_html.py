import os

# 获取当前目录下所有的文件名
file_list = os.listdir()

# 筛选出所有的html文件名
html_files = [file for file in file_list if file.endswith('.html')]

# 将html文件名保存到name_html.txt中
with open('name_html.txt', 'w') as file:
    for html_file in html_files:
        file.write(html_file + '\n')
