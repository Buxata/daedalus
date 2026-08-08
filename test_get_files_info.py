# test_get_files_info.py
import unittest

from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def test_current_directory(self):
        output = get_files_info("calculator", "")
        self.assertTrue(output.startswith("Result for current directory:"))

    def test_subdirectory(self):
        output = get_files_info("calculator", "pkg")
        self.assertTrue(output.startswith("Result for 'pkg' directory:"))
        print(output)

    def test_absolute_path_outside(self):
        output = get_files_info("calculator", "/bin")
        self.assertTrue(output.startswith("Result for '/bin' directory:"))
        print(output)

    def test_parent_directory(self):
        output = get_files_info("calculator", "../")
        self.assertTrue(output.startswith("Result for '../' directory:"))
        print(output)

    def test_non_directory_input(self):
        output = get_files_info("calculator", "not_a_dir")
        self.assertTrue(output.startswith("Result for 'not_a_dir' directory:"))
        print(output)


if __name__ == "__main__":
    unittest.main()
