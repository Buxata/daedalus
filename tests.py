import os
import unittest

from functions.get_files_info import get_files_info


class TestGetFilesInfoBegins(unittest.TestCase):


    def test_current_directory_begin(self):
        output = get_files_info("calculator", ".")
        self.assertTrue(output.startswith("Result for current directory:"))
        print(output)


    def test_subdirectory_begin(self):
        output = get_files_info("calculator", "pkg")
        self.assertTrue(output.startswith("Result for 'pkg' directory:"))
        print(output)

    def test_absolute_path_outside_begin(self):
        output = get_files_info("calculator", "/bin")
        self.assertTrue(output.startswith("Result for '/bin' directory:"))
        print(output)

    def test_parent_directory_begin(self):
        output = get_files_info("calculator", "../")
        self.assertTrue(output.startswith("Result for '../' directory:"))
        print(output)

    def test_calculators_parent_not_directory_begin(self):
        output = get_files_info("calculators","../")
        self.assertTrue(output.startswith("Result for '../' directory:"))
        print(output)


if __name__ == '__main__':
    unittest.main()
