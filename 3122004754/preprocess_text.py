import jieba
import string


def preprocess_text(text):
    # 去除标点符号
    text = ''.join(ch for ch in text if ch not in string.punctuation)
    # 分词
    words = jieba.lcut(text)
    # 返回以空格分隔的词汇字符串
    return ' '.join(words)