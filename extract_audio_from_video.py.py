from moviepy.editor import VideoFileClip

try:
    # 加载视频文件
    video = VideoFileClip('目标视频文件.mp4')
    
    # 获取视频中的音频
    audio = video.audio
    
    # 将音频写入到mp3文件
    audio.write_audiofile('我是生成的音频.mp3')
    
    # 释放资源
    video.close()
    audio.close()
    
    print("音频提取成功！")
except Exception as e:
    print(f"发生错误：{e}")
