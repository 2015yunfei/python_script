from pydub import AudioSegment

# 加载第一个MP3文件（假设时长较短）
audio1 = AudioSegment.from_file("175BPM.mp3")

# 加载第二个MP3文件（假设时长较长）
audio2 = AudioSegment.from_file("music.mp3")

# 调整音量（增加或减少分贝）
audio1 -= 7  # 增加音量

# 确定两个音频的长度
len_audio1 = len(audio1)
len_audio2 = len(audio2)

# 找出较长的音频和较短的音频
longest_audio = audio1 if len_audio1 > len_audio2 else audio2
shortest_audio = audio2 if len_audio1 > len_audio2 else audio1

# 计算需要重复的次数
repeats = int((len(longest_audio) / len(shortest_audio)) + 1)

# 通过重复较短的音频来匹配较长的音频时长
combined = shortest_audio
for _ in range(repeats - 1):
    combined += shortest_audio

# 确保组合音频与最长音频长度一致
combined = combined[:len(longest_audio)]

# 将两个音频文件叠加
combined = combined.overlay(longest_audio)

# 导出合并后的音频文件
combined.export("result.mp3", format="mp3")
