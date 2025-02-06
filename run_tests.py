import unittest

def run_all_tests():
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    suite.addTests(loader.discover('./tests', pattern='test_*.py'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
