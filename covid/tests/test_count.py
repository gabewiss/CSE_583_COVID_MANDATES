"""
This module is the unittest for the count_processing function

UnitTests(unittest.TestCase) -- framework for functions testing
                                Exports 'OK', 'FAIL',
                                or 'ERROR'
"""

import unittest
import pandas as pd


from src import count_processing as cp
import pandas.testing as pd_testing


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
        one_shot_date = ["2020-1-20", "2020-2-13", "2020-3-20"]
        one_shot_case = [1, 2, 3]
        one_shot_death = [1, 2, 3]
        one_shot_pop = [100000, 200000, 300000]
        one_shot_month = [1, 2, 3]
        one_shot_new_case = [1, 2, 3]
        one_shot_new_death = [1, 2, 3]
        one_shot_state = ['CA', 'TX', 'WA']
        one_shot_new_case_norm = [1, 1, 1]
        one_shot_new_death_norm = [1, 1, 1]
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
        self.one_shot_df =\
            pd.DataFrame(list(zip(one_shot_state, one_shot_date,
                                  one_shot_case, one_shot_death)),
                         columns=['state', 'submission_date',
                         'new_case', 'new_death'])
        self.one_shot_pop_df =\
            pd.DataFrame(list(zip(one_shot_state, one_shot_pop)),
                         columns=['state_id', 'population'])

        self.one_shot_monthly_df =\
            pd.DataFrame(list(zip(one_shot_state, one_shot_month,
                                  one_shot_new_case,
                                  one_shot_new_death, one_shot_pop,
                                  one_shot_new_case_norm,
                                  one_shot_new_death_norm)),
                         columns=['state', 'month', 'new_case',
                                  'new_death', 'population',
                                  'new_case_norm', 'new_death_norm'])

    # smoke test
    def test_cp_raise_no_error(self):
        """
        A smoke test to see if the function works correctly
        """
        try:
            cp.count_processing(self.correct_df, self.pop_df)
        except KeyError:
            self.fail("Raise exception unexpectedly!")

    # one-shot test
    def test_cp_compare_expected_result(self):
        """
        An one-shot test to see if the function gives the expected result
        """
        pd_testing.assert_frame_equal(
            cp.count_processing(self.one_shot_df, self.one_shot_pop_df)[1],
            self.one_shot_monthly_df,
            check_dtype=False)

    # edge test
    def test_cp_raise_correct_error(self):
        """
        An edge test to see if it raises the correct error
        """
        with self.assertRaises(KeyError):
            cp.count_processing(self.wrong_df, self.pop_df)


if __name__ == '__main__':
    unittest.main()
