"""
2024年7月15日
实习工作
在两个不同的表中匹配关键字，将对应数据从一个表中写入到另外一个表
"""

import openpyxl

# 假设已经有一个名为 'workbook.xlsx' 的工作簿，其中包含 'sheet1' 和 'sheet2'
workbook = openpyxl.load_workbook('1.xlsx')
sheet1 = workbook['sheet1']
sheet2 = workbook['Sheet2']

# 遍历sheet2中的服务名称和数字
for i in range(2, 132):  # 从第2行到第132行
    service_name = sheet2[f'F{i}'].value  # 获取sheet2中的服务名称
    number = sheet2[f'H{i}'].value  # 获取sheet2中的数字

    # 在sheet1中查找匹配的服务名称
    for j in range(2, 133):
        if sheet1[f'D{j}'].value == service_name:
            sheet1[f'F{j}'].value = number  # 将数字复制到sheet1中对应的位置
            print("has find " + service_name)
            break  # 找到匹配项后跳出内层循环

# 保存工作簿
workbook.save('workbook.xlsx')
