import unittest
import os
import tempfile
import shutil
from unittest.mock import patch
from functions.get_files_info import get_files_info

class TestMain(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory structure for testing
        self.test_dir = tempfile.mkdtemp()
        self.calculator_dir = os.path.join(self.test_dir, "calculator")
        os.makedirs(self.calculator_dir)
        
        # Create some test files and directories
        with open(os.path.join(self.calculator_dir, "test_file.txt"), "w") as f:
            f.write("test content")
        
        pkg_dir = os.path.join(self.calculator_dir, "pkg")
        os.makedirs(pkg_dir)
        with open(os.path.join(pkg_dir, "module.py"), "w") as f:
            f.write("# test module")
    
    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)
    
    def test_current_directory(self):
        """Test listing current directory"""
        with patch('builtins.print') as mock_print:
            get_files_info(self.calculator_dir, ".")
            # Check that print was called (files were listed)
            self.assertTrue(mock_print.called)
    
    def test_subdirectory(self):
        """Test listing subdirectory"""
        with patch('builtins.print') as mock_print:
            get_files_info(self.calculator_dir, "pkg")
            # Check that print was called
            self.assertTrue(mock_print.called)
    
    def test_absolute_path_outside_working_dir(self):
        """Test that absolute paths outside working directory are rejected"""
        with patch('builtins.print') as mock_print:
            get_files_info(self.calculator_dir, "/bin")
            # Check that error message was printed
            mock_print.assert_called_with('Error: Cannot list "/bin" as it is outside the permitted working directory')
    
    def test_parent_directory_access(self):
        """Test that parent directory access is blocked"""
        with patch('builtins.print') as mock_print:
            get_files_info(self.calculator_dir, "../")
            # Check that error message was printed
            mock_print.assert_called_with('Error: Cannot list "../" as it is outside the permitted working directory')
    
    def test_nonexistent_directory(self):
        """Test handling of non-existent directory"""
        with patch('builtins.print') as mock_print:
            get_files_info(self.calculator_dir, "nonexistent")
            # Should print error about not being a directory
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()