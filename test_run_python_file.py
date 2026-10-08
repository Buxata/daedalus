# test_get_files_info.py
import unittest

from functions.run_python_file import run_python_file


class TestGetFilesInfo(unittest.TestCase):
    def test_running_no_args(self):
        output = run_python_file("calculator", "main.py")
        self.assertTrue(output.__contains__("Calculator App"))
        print(output)

    def test_running_args(self):
        output = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertTrue(output.__contains__("3 + 5 "))
        print(output)

    def test_running_tests(self):
        output = run_python_file("calculator", "tests.py")
        self.assertTrue(output.__contains__("tests in "))
        print(output)

    def test_outside_absolute_path(self):
        output = run_python_file("calculator", "../main.py")
        self.assertTrue(output.__contains__("as it is outside the permitted working directory"))
        print(output)

    def test_run_non_py_file(self):
        output = run_python_file("calculator", "lorem.txt")
        self.assertTrue(output.__contains__("is not a Python file"))
        print(output)

    def test_absolute_path_outside(self):
        output = run_python_file("calculator", "nonexistent.py")
        self.assertTrue(output.__contains__("does not exist or is not a regular file"))
        print(output)

if __name__ == "__main__":
    unittest.main()
