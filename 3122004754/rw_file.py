def read_file(file_path):  # 读取原文件和待查重文件的内容，并转化为字符串
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_result(file_path, result):  # 输出查重结果
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"{result:.2f}\n")  # 结果保留两位小数