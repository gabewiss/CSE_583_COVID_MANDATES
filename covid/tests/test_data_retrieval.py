import unittest

import pandas as pd

import data_retrieval

class TestDataRetrieval(unittest.TestCase):
    """Test the data retrieval function"""

    def test_smoke1(self):
        """
        Smoke test on data_retrieval
        """
        self.assertTrue(data_retrieval(True))


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
