import unittest

def run_all_tests():
    """
        Runs all the tests found in the './tests' directory that match the pattern 'test_*.py'.
        
        This function:
        1. Initializes a TestSuite to hold the test cases.
        2. Uses a TestLoader to discover all test files that start with 'test_' in the './tests' directory.
        3. Adds the discovered test cases to the suite.
        4. Creates a TextTestRunner to run the tests and display the results in the console.
    """
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    suite.addTests(loader.discover('./tests', pattern='test_*.py'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
