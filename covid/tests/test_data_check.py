"""
Unittest module to test data_check module

TestDataRetrieval(unittest.TestCase) -- class containing a smoke test,
two one-shot tests, and two edge tests for data_check module.

test_smoke(self) -- function tests repo_check using self.assertTrue
test_address(self) -- make sure data URL is correct
________________________________________
Author: Gabriel Wisswaesser
"""
import unittest

import data_check


class TestDataRetrieval(unittest.TestCase):
    """Test the data_retrieval function"""

    def test_smoke(self):
        """
        Smoke test on repo_check to see if data repos return
        HTTP Status Code 200.
        """
        self.assertTrue(data_check.repo_check(),)

    def test_address(self):
        """
        pseudo one-shot/smoker to check address for data are correct
        """


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
