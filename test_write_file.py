# test_get_files_info.py
import unittest

from functions.write_file import write_file


class TestGetFilesInfo(unittest.TestCase):
    def test_current_directory(self):
        output = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        self.assertTrue(output.startswith("Successfully wrote to "))
        print(output)

    def test_subdirectory(self):
        output = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        self.assertTrue(output.startswith("Successfully wrote to "))
        print(output)

    def test_absolute_path_outside(self):
        output = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        self.assertTrue(output.__contains__("s it is outside the permitted working directory"))
        print(output)

if __name__ == "__main__":
    unittest.main()
