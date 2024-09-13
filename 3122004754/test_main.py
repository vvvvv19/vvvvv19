import unittest
import main_for_test as main

class TestMain(unittest.TestCase):
    #测试两个相同的文本
    def test_identical_file(self):
        text1 = "orig.txt"
        text2 = "orig.txt"
        text3 = "textfile.txt"
        print("测试两个相同的文本:")
        print(main.main(text1, text2,text3))
        self.assertAlmostEqual(main.main(text1, text2,text3), 1.0)

    def test_partially_similar_texts1(self):
        #测试待查重文本字数少于原文本的情况
        text1 = "orig.txt"
        text2 = "orig_0.8_del.txt"
        text3 = "textfile.txt"
        print("测试待查重文本字数少于原文本的情况:")
        print(main.main(text1, text2, text3))
        self.assertGreater(main.main(text1, text2, text3), 0.0)  # 预期相似度大于 0.0
        self.assertLess(main.main(text1, text2, text3), 1.0)  # 预期相似度小于 1.0

    def test_partially_similar_texts2(self):
        #测试待查重文本字数多于原文本的情况
        text1 = "orig.txt"
        text2 = "orig_0.8_add.txt"
        text3 = "textfile.txt"
        print("测试待查重文本字数多于原文本的情况:")
        print(main.main(text1, text2, text3))
        self.assertGreater(main.main(text1, text2, text3), 0.0)  # 预期相似度大于 0.0
        self.assertLess(main.main(text1, text2, text3), 1.0)  # 预期相似度小于 1.0

    def test_partially_similar_texts3(self):
        #测试待查重文本不同与原文本的情况
        text1 = "orig.txt"
        text2 = "orig_0.8_dis_10.txt"
        text3 = "textfile.txt"
        print("测试待查重文本不同于原文本的情况:")
        print(main.main(text1, text2, text3))
        self.assertGreater(main.main(text1, text2, text3), 0.0)  # 预期相似度大于 0.0
        self.assertLess(main.main(text1, text2, text3), 1.0)  # 预期相似度小于 1.0

    def test_partially_similar_texts4(self):
        #测试待查重文本远远少于原文本的情况
        text1 = "orig.txt"
        text2 = "orig_0.8_short.txt"
        text3 = "textfile.txt"
        print("测试待查重文本远远少于原文本的情况:")
        print(main.main(text1, text2, text3))
        self.assertGreater(main.main(text1, text2, text3), 0.0)  # 预期相似度大于 0.0
        self.assertLess(main.main(text1, text2, text3), 1.0)  # 预期相似度小于 1.0

    def test_empty_text(self):
        #测试空文本
        text1 = "empty.txt"
        text2 = "orig.txt"
        text3 = "textfile.txt"
        print("测试空文本:")
        print(main.main(text1, text2, text3))
        self.assertEqual(main.main(text1, text2, text3), 0.0)  # 预期相似度为 0.0

if __name__ == '__main__':
    unittest.main()
