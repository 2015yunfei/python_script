import os

# 支持的视频文件格式列表
video_formats = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.mpeg', '.3gp', '.webm', '.ogg']


def find_videos(directory):
    videos = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in video_formats:
                videos.append(os.path.relpath(os.path.join(root, file), directory))
    return videos


def main():
    current_directory = os.getcwd()
    videos = find_videos(current_directory)

    with open('path.txt', 'w') as f:
        for video in videos:
            f.write(video + '\n')

    print(f"视频路径已保存到 {os.path.join(current_directory, 'path.txt')}")


if __name__ == "__main__":
    main()
