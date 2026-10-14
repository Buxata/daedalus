import sys
import unittest

def run_all_tests():
    # Discover and run all test files matching "test*.py" in the "tests" directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return exit code 1 if any tests failed or errored so subprocess/CI picks it up
    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == "__main__":
    run_all_tests()
