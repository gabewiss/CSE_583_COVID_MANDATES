"""
Unittest module to test data_check module

TestDataRetrieval(unittest.TestCase) -- class containing a smoke test,
two one-shot tests, and two edge tests for data_check module.

test_smoke(self) -- function tests repo_check using self.assertTrue

"""
import unittest

import data_check


class TestDataRetrieval(unittest.TestCase):
    """Test the data_retrieval function"""

    def smoke_test(self):
        """
        Smoke test on repo_check
        """
        self.assertTrue(data_check.repo_check(),)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
