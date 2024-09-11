def calculate_jaccard_similarity(text1, text2):
    # 从处理好的文本中提取出所有的单词，并将这些单词存储在一个集合中
    set1 = {word for word in text1.split()}
    set2 = {word for word in text2.split()}
    # 计算交集
    intersection = len(set1 & set2)
    # 计算并集
    union = len(set1 | set2)
    # 计算Jaccard相似度并输出
    return intersection / union