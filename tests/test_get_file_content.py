# test_get_files_info.py
import unittest

from functions.get_file_content import get_file_content

class TestGetFilesContent(unittest.TestCase):
    def test_lorem(self):
        result = get_file_content("calculator", "lorem.txt")
        print(result)
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        self.assertTrue('truncated' in result)

    def test_main_file(self):
        result = get_file_content("calculator", "main.py")
        self.assertTrue(result.startswith('Result for \'main.py\''))


    def test_calc_file(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertTrue(result.startswith("Result for 'pkg/calculator.py'"))

    def test_oustide_dir(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertTrue(result.__contains__('Error: Cannot read "'))

    def test_non_existent_file(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertTrue(result.__contains__("Error: File not found or is not a regular file:"))

    # def test_pass(self):
    #     print("def main() -> None:")
    #     print("Error:")
    #     print("def _apply_operator(self, operators: list[str], values: list[float])")
    #     print("pkg/does_not_exist.py")

if __name__ == "__main__":
    unittest.main()
