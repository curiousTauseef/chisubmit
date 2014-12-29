from . import test_courses
from unittest.suite import TestSuite

test_cases = [test_courses]

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_module in test_cases:
        tests = loader.loadTestsFromModule(test_module)
        suite.addTests(tests)
    return suite