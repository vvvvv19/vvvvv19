import unittest
import rw_file as rw
import os

class TestRWFile(unittest.TestCase):
    def setUp(self):
        self.test_input_file = 'test_input.txt'
        self.test_output_file = 'test_output.txt'

        # Create a test input file with known content
        with open(self.test_input_file, 'w', encoding='utf-8') as f:
            f.write("This is a test.")

    def test_read_file(self):
        # Test reading from the file
        content = rw.read_file(self.test_input_file)
        self.assertEqual(content, "This is a test.")

    def test_write_result(self):
        # Test writing to the file
        rw.write_result(self.test_output_file, 0.85)
        with open(self.test_output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, "0.85\n")

    def tearDown(self):
        # Clean up files after tests
        if os.path.isfile(self.test_input_file):
            os.remove(self.test_input_file)
        if os.path.isfile(self.test_output_file):
            os.remove(self.test_output_file)

if __name__ == '__main__':
    unittest.main()
