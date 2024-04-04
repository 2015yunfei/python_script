import os


def rename_videos():
    video_files = [f for f in os.listdir('.') if
                   os.path.isfile(f) and f.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'))]
    # 列出当前目录下所有视频文件

    for i, video_file in enumerate(video_files):
        # 重命名每个视频文件为数字形式
        new_name = f"{i + 1}.{'.'.join(video_file.split('.')[1:])}"
        os.rename(video_file, new_name)
        print(f"Renamed {video_file} to {new_name}")


if __name__ == "__main__":
    rename_videos()
