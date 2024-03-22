import os
import send2trash


def move_html_files_to_trash(directory):
    # 获取目录中所有文件和文件夹
    items = os.listdir(directory)

    for item in items:
        # 构建文件/文件夹的完整路径
        item_path = os.path.join(directory, item)

        # 如果是文件夹，则递归调用 move_html_files_to_trash
        if os.path.isdir(item_path):
            move_html_files_to_trash(item_path)
        else:
            # 如果是HTML文件，则移动到回收站
            if item_path.endswith('.html'):
                send2trash.send2trash(item_path)
                print(f"Moved to trash: {item_path}")


# 当前目录
current_directory = os.getcwd()
move_html_files_to_trash(current_directory)
