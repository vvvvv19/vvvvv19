import jieba
import string

# 停用词列表（示例，实际使用时可以根据需求调整）
stop_words = {'的', '了', '是', '很', '我', '有', '和', '也', '你', '们', '他', '她'}


def preprocess_text(text):
        # 定义标点符号集合
        punctuation = set(string.punctuation + "，。！？；：“”‘’（）【】《》")
        # 分词
        words = jieba.lcut(text)
        # 去除标点符号和停用词
        filtered_words = [word for word in words if word not in punctuation and word not in stop_words]
        # 返回以空格分隔的词汇字符串
        return ' '.join(filtered_words)