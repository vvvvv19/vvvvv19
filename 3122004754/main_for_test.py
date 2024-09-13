import rw_file as rw
import preprocess_text as pre
import calculate_jaccard_similarity as jacsim
import calculate_cosine_similarity as cossim

def main(original_file,plagiarized_file,output_file):
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
    rw.write_result(output_file,all_score)

    return  all_score