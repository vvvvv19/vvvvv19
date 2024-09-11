import sys
import rw_file as rw
import preprocess_text as pre
import calculate_jaccard_similarity as jacsim

def main():
    if len(sys.argv) != 4:  # 确保用户按照正确的格式提供了所需的文件路径，否则终止运行
        print("Usage: python script.py <original_file> <plagiarized_file> <output_file>")
        sys.exit(1)

    # 命令行导入文本
    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    # 读取文件内容
    original_text = rw.read_file(original_file)
    plagiarized_text = rw.read_file(plagiarized_file)

    # 文本预处理
    original_text_processed = pre.preprocess_text(original_text)
    plagiarized_text_processed = pre.preprocess_text(plagiarized_text)

    # 计算 Jaccard 相似度
    jaccard_similarity = jacsim.calculate_jaccard_similarity(original_text_processed, plagiarized_text_processed)
    rw.write_result(output_file, jaccard_similarity)
    print(jaccard_similarity)

#执行main函数
if __name__ == "__main__":
    main()