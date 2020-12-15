"""
Unittest module to test data_check module

TestDataRetrieval(unittest.TestCase) -- class containing two smoke tests,
and an edge tests for data_check module.

test_smoke_url(self) -- tests repo_check using self.assertTrue
test_smoke_object_check(self) -- tests object_check using
                                 self.assertTrue
test_edge_object_check(self) -- tests object_check if numpy array is used

________________________________________
Author: Gabriel Wisswaesser
"""
import pandas as pd
import unittest

import data_check


class TestDataRetrieval(unittest.TestCase):
    """
    Test the data_retrieval function repo_check and object_check
    """

    def test_smoke_count_vet(self):
        """
        Smoke test on count_data_vet_import to see if it runs
        """
        state_count = data_check.count_data_vet_import()
        isinstance(state_count, pd.DataFrame)

    def test_smoke_mandate_vet(self):
        """
        Smoke test on count_data_vet_import to see if it runs
        """
        state_mandate = data_check.mandate_data_vet_import()
        isinstance(state_mandate, pd.DataFrame)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
