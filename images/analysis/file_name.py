import os

def get_all_files(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_names.append(file_name)
    return file_names

# 用法示例
folder_path = r"nidewenjian"  # 替换为实际的文件夹路径
file_names = get_all_files(folder_path)
for file_name in sorted(file_names):
    print(file_name)

