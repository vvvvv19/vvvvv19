from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(text1, text2):  # 计算余弦相似度
    # 初始化 TF-IDF 向量化器
    vectorizer = TfidfVectorizer()

    # 将文本转化为 TF-IDF 矩阵
    # fit_transform() 方法会学习文本数据的词汇表并将文本转换为 TF-IDF 矩阵
    # 这里的 [text1, text2] 是一个文本列表
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # 计算两个文本之间的余弦相似度
    # cosine_similarity() 方法接受两个矩阵作为输入，这里分别是 tfidf_matrix[0:1] 和 tfidf_matrix[1:2]
    # tfidf_matrix[0:1] 代表第一个文本的 TF-IDF 向量
    # tfidf_matrix[1:2] 代表第二个文本的 TF-IDF 向量
    # 计算结果是一个 1x1 的矩阵，包含两个文本之间的余弦相似度值
    # [0][0] 提取这个相似度值
    return min(max(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0], 0.0), 1.0)  # 确保结果在 [0, 1] 范围内,避免因精度问题结果大于1的情况
