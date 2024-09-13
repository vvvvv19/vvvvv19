import jieba
import string
import re

# 停用词列表（示例，实际使用时可以根据需求调整）
stop_words = {'的', '了', '是', '很', '我', '有', '和', '也', '你', '们', '他', '她'}

def preprocess_text(text):
    # 定义标点符号集合，包括英文和中文标点
    punctuation = string.punctuation + "，。！？；：“”‘’（）【】《》"
    # 转义标点符号中的特殊字符
    escaped_punctuation = re.escape(punctuation)
    # 处理标点符号，替换为单个空格
    text = re.sub(f"[{escaped_punctuation}]", ' ', text)
    # 使用 jieba 对中文部分进行分词
    words = jieba.lcut(text)
    # 去除停用词和处理英文单词（去除英文标点）
    processed_words = []
    for word in words:
        # 处理英文单词
        if re.match(r'[a-zA-Z]+', word):
            word = re.sub(f"[{string.punctuation}]", '', word)
        # 只保留非停用词且不为空的词
        if word.strip() and word not in stop_words:
            processed_words.append(word)
    # 返回以空格分隔的词汇字符串
    return ' '.join(processed_words)