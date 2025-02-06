import unittest

def run_all_tests():
    # Create a test suite
    suite = unittest.TestSuite()

    # Load tests from your test files
    loader = unittest.TestLoader()

    # Add tests from each of the test files
    suite.addTests(loader.discover('./tests', pattern='test_*.py'))

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
