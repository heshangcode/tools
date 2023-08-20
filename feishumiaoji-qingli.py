# 飞书妙记才有文字记录后面的内容
import os

def process_text_files(folder_path):
    # 获取目标路径下的所有文件
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # 遍历每个文件
    for file_name in file_list:
        # 确保文件是以.txt结尾的文本文件
        if file_name.lower().endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                content = file.read()
            
            # 查找关键词的位置
            index = content.find("文字记录:")
            if index != -1:
                # 保留关键词后面的内容
                processed_content = content[index+5:]
                
                # 将处理后的内容写回文件
                with open(file_path, "w") as file:
                    file.write(processed_content)

# 指定目标路径
# target_folder = os.path.expanduser("/Users/heshang/Movies/纪元的早起优酷视频")
target_folder = os.path.expanduser("~/Documents/ky妙记")
# target_folder = os.path.expanduser("/Users/heshang/Documents/每日正念-txt")

# 调用函数进行处理
process_text_files(target_folder)