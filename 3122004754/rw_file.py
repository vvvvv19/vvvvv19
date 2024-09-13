import sys

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        #文件不存在时退出程序
        print(f"文件 '{file_path}' 不存在。")
        sys.exit(1)
    except IOError as e:
        #文件读取错误是退出程序
        print(f"读取文件 '{file_path}' 时出错: {e}")
        sys.exit(1)

def write_result(file_path, result):
    try:
        #文件不存在时创建新文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{result:.2f}\n")
    except IOError as e:
        #写入错误时退出程序
        print(f"写入文件 '{file_path}' 时出错: {e}")
        sys.exit(1)
