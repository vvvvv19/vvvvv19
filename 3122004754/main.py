import sys
import os
import re
import threading
import rw_file as rw
import preprocess_text as pre
import calculate_jaccard_similarity as jacsim
import calculate_cosine_similarity as cossim

# 超时异常
class TimeoutException(Exception):
    pass

# 超时处理函数
def timeout_handler():
    raise TimeoutException("程序运行时间超过限制")

def main():
    if len(sys.argv) != 4:  # 确保用户按照正确的格式提供了所需的文件路径，否则终止运行
        print("Usage: python script.py <original_file> <plagiarized_file> <output_file>")
        sys.exit(1)

    # 命令行导入文本
    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    # 设置超时处理器
    timer = threading.Timer(5.0, timeout_handler)
    timer.start()

    try:
        # 读取文件内容
        original_text = rw.read_file(original_file)
        plagiarized_text = rw.read_file(plagiarized_file)

        # 文本预处理
        original_text_processed = pre.preprocess_text(original_text)
        plagiarized_text_processed = pre.preprocess_text(plagiarized_text)

        # 计算 Jaccard 相似度
        jaccard_similarity = jacsim.calculate_jaccard_similarity(original_text_processed, plagiarized_text_processed)
        # 计算余弦相似度
        cosine_similarity_score = cossim.calculate_cosine_similarity(original_text_processed, plagiarized_text_processed)

        #综合两者的结果，通过加权将两种相似度结果结合起来，以获得综合相似度评分
        #这里Jaccard 相似度权重为 20%，余弦相似度权重为 80%
        all_score=0.2*jaccard_similarity+cosine_similarity_score*0.8
        print("查重率为:" + str(all_score))
        rw.write_result(output_file,all_score)

    except TimeoutException:
        print("程序超时，退出程序")
        sys.exit(1)
    finally:
        # 取消定时器
        timer.cancel()

#执行main函数
if __name__ == "__main__":
    main()