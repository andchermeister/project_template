import unittest
import pandas as pd
from app.io.input import read_from_file_original, read_from_file_pandas

class TestInputFunctions(unittest.TestCase):
    def test_read_from_file_original(self):
        path_to_file = "/Users/...project_template/project_template/data/file_to_input.txt"
        content = "File to input data..."
        with open(path_to_file, 'w') as f:
            f.write(content)

        result = read_from_file_original('data/file_to_input.txt')

        self.assertEqual(result, content)

    def test_read_from_file_pandas(self):
        path_to_file = "/Users/...project_template/project_template/data/file_for_pandas.txt"
        content = "A,B,C\n1,2,3\n4,5,6\n"
        with open(path_to_file, 'w') as f:
            f.write(content)

        result = read_from_file_pandas('data/file_for_pandas.csv')


        expected_result = pd.DataFrame({'A': [1, 4], 'B': [2, 5], 'C': [3, 6]})
        pd.testing.assert_frame_equal(result, expected_result)


if __name__ == '__main__':
    unittest.main()
