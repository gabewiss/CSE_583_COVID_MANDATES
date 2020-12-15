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
import numpy as np
import unittest

import data_check


class TestDataRetrieval(unittest.TestCase):
    """
    Test the data_retrieval function repo_check and object_check
    """

    def test_smoke_repo_check(self):
        """
        Smoke test on repo_check to see if data repos return
        HTTP Status Code 200.
        """
        self.assertTrue(data_check.repo_check(),)

    def test_smoke_object_check(self):
        """
        Test object_check
        """
        state_count = pd.read_csv('https://raw.githubusercontent.com'
                                  '/nytimes/covid-19-data/master/'
                                  'us-states.csv')
        state_mandate = pd.read_csv('https://healthdata.gov/'
                                    'sites/default/files/'
                                    'state_policy_updates_20201202_0721.csv')
        self.assertTrue(data_check.object_check(state_count, state_mandate), )

    def test_edge_object_check(self):
        """
        Test object_check using a numpy array and assertTrue and
        isinstance to check if the string is returned when numpy array
        triggers
        """
        state_count = np.array([[4, 7], [15, 18],
                                [18, 21], [13, 19],
                                [10, 15], [7, 12],
                                [4, 6], [5, 9],
                                [8, 10], [9, 14],
                                [13, 15], [11, 12],
                                [12, 17]])
        state_mandate = np.array([[4, 7], [15, 18],
                                 [18, 21], [13, 19],
                                 [10, 15], [7, 12],
                                 [4, 6], [5, 9],
                                 [8, 10], [9, 14],
                                 [13, 15], [11, 12],
                                 [12, 17]])
        self.assertTrue(isinstance(data_check.object_check
                                   (state_count, state_mandate), str))


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
