import unittest
import calculate_cosine_similarity as cossim
import calculate_jaccard_similarity as jacsim

# 使用 unittest 框架进行单元测试
class TestCosineSimilarity(unittest.TestCase):
    # 测试两个完全相同的文本
    def test_identical_texts(self):
        text1 = "明天的天气会很晴朗"
        text2 = "明天的天气会很晴朗"
        # 相似度应该接近 1
        self.assertAlmostEqual(jacsim.calculate_jaccard_similarity(text1, text2), 1.0)
        self.assertAlmostEqual(cossim.calculate_cosine_similarity(text1, text2), 1.0)

    # 测试两个含有不同但相关的文本
    def test_different_texts(self):
        text1 = "明天的 天气 会很 晴朗"
        text2 = "明天 会有 一个 很晴朗的 天气"
        # 相似度应该大于 0，但小于 1
        self.assertGreater(jacsim.calculate_jaccard_similarity(text1, text2), 0)
        self.assertGreater(cossim.calculate_cosine_similarity(text1, text2), 0)

    # 测试两个完全不同的文本
    def test_completely_different_texts(self):
        text1 = "苹果 是 水果"
        text2 = "电影 是 娱乐"
        # 相似度应该接近 0
        self.assertAlmostEqual(jacsim.calculate_jaccard_similarity(text1, text2), 0.0)
        self.assertAlmostEqual(cossim.calculate_cosine_similarity(text1, text2), 0.0)

if __name__ == "__main__":
    # 运行测试
    unittest.main()
