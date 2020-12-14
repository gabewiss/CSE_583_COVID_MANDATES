"""
This module is the unittest for the count_processing function

UnitTests(unittest.TestCase) -- framework for functions testing
                                Exports 'OK', 'FAIL',
                                or 'ERROR'
"""

import unittest
import pandas as pd

from src import count_processing as cp


class CountTest(unittest.TestCase):
    """
    Class to test the count_processing function. It includs
    smoke test, one-shot test, and edge test
    """
    def setUp(self):
        """
        Constructor to declare the correct and incorrect
        dataframe for testing
        """
        state = ['CA', 'WA', 'TX']
        date = ["2020-10-20", "2020-04-13", "2020-11-20"]
        case = [100, 200, 300]
        death = [10, 1, 30]
        pop = [10000, 200000, 3000]
        self.correct_df =\
            pd.DataFrame(list(zip(state, date, case, death)),
                         columns=['state', 'submission_date',
                         'new_case', 'new_death'])
        self.wrong_df =\
            pd.DataFrame(list(zip(state, date, case)),
                         columns=['state', 'submission_date',
                         'new_case'])
        self.pop_df =\
            pd.DataFrame(list(zip(state, pop)),
                         columns=['state_id', 'population'])

    # smoke test
    def test_cp_raise_no_error(self):
        """
        """
        try:
            cp.count_processing(self.correct_df, self.pop_df)
        except KeyError:
            self.fail("Raise exception unexpectedly!")
    # one-shot test

    # edge test
    def test_cp_raise_correct_error(self):
        """
        """
        with self.assertRaises(KeyError):
            cp.count_processing(self.wrong_df, self.pop_df)


if __name__ == '__main__':
    unittest.main()
