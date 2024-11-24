import subprocess
import os
import shutil

# 定义要执行的文件路径
scripts = [
    "E:\\tk\\build_json_delete_duplicates.py",
    "E:\\tkk\\delete_duplicates_from_json.py",
    "E:\\tkk\\build_json_delete_duplicates.py"
]

# 第一个脚本执行完成后要移动的文件
source_file = "E:\\tk\\files_sha1.json"
destination = "E:\\tkk\\files_sha1.json"

# 输出重定向的文件
output_log = "D:\\output.log"

# 打开日志文件，准备写入
with open(output_log, 'w') as log_file:
    # 顺序执行每个脚本
    for i, script in enumerate(scripts):
        try:
            # 使用subprocess.run来执行脚本，并重定向输出到日志文件
            subprocess.run(["python", script], check=True, stdout=log_file, stderr=subprocess.STDOUT)
            print(f"脚本 {script} 执行成功。", file=log_file)

            # 在执行完第一个脚本后，移动文件
            if i == 0 and os.path.exists(source_file):
                shutil.move(source_file, destination)
                print(f"文件 {source_file} 已移动到 {destination}", file=log_file)
            elif i == 0 and not os.path.exists(source_file):
                print(f"错误：文件 {source_file} 不存在，无法移动。", file=log_file)
                break  # 如果文件不存在，则中断执行
        except subprocess.CalledProcessError as e:
            print(f"脚本 {script} 执行失败，错误信息：{e}", file=log_file)
            break  # 如果脚本执行失败，则中断执行

print(f"所有操作执行完毕", file=log_file)