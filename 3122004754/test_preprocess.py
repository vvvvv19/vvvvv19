import unittest
import preprocess_text as pre

class TestPreprocessText(unittest.TestCase):

    def test_only_chinese(self):
        text = "我喜欢学习编程。"
        expected = "喜欢 学习 编程"
        self.assertEqual(pre.preprocess_text(text), expected)

    def test_only_english(self):
        text = "I love programming."
        expected = "I love programming"
        self.assertEqual(pre.preprocess_text(text), expected)

    def test_mixed_chinese_english(self):
        text = "我喜欢 coding in Python。"
        expected = "喜欢 coding in Python"
        self.assertEqual(pre.preprocess_text(text), expected)

    def test_punctuation(self):
        text = "你好，世界！Hello, world!"
        expected = "你好 世界 Hello world"
        self.assertEqual(pre.preprocess_text(text), expected)

    def test_stop_words(self):
        text = "我很喜欢这个产品。"
        expected = "喜欢 这个 产品"
        self.assertEqual(pre.preprocess_text(text), expected)

    def test_empty_string(self):
        text = ""
        expected = ""
        self.assertEqual(pre.preprocess_text(text), expected)

    def test_all_stop_words(self):
        text = "我 和 他 是 了"
        expected = ""
        self.assertEqual(pre.preprocess_text(text), expected)

if __name__ == "__main__":
    unittest.main()

