import unittest

import pandas as pd

from covid import data_check

class TestDataRetrieval(unittest.TestCase):
    """Test the data_retrieval function"""

    def smoke_test(self):
        """
        Smoke test on data_retrieval
        """


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
