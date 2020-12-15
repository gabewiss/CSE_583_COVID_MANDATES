"""
This module is the unittest for the mandate_processing function

"""

import unittest
import pandas as pd

from src import mandate_processing as mp


class CountTest(unittest.TestCase):
    """
    Class to test the mandate_processing function. It includes
    a smoke test and an edge test
    """
    def setUp(self):
        """
        Constructor to declare the correct and incorrect
        dataframe for testing
        """
        state_id = ['CA', 'WA', 'TX']
        state_id_wrong = ['CC', 'WA', 'TX']
        policy_level = ['state', 'state', 'county']
        date = ["2020-10-20", "2020-04-13", "2020-11-20"]
        policy_type = ["Shelter in Place", 'Outdoor and Recreation',
                       "Food and Drink"]
        start_stop = ['start', 'start', 'stop']
        self.correct_df =\
            pd.DataFrame(list(zip(state_id, policy_level, date,
                         policy_type, start_stop)),
                         columns=['state_id', 'policy_level',
                         'date', 'policy_type', 'start_stop'])
        self.wrong_df =\
            pd.DataFrame(list(zip(state_id_wrong, policy_level, date,
                         policy_type, start_stop)),
                         columns=['state_id_wrong', 'policy_level',
                         'date', 'policy_type', 'start_stop'])

    def test_mp_raiseNoError(self):
        """
        Smoke test to check whether this function catches fire
        """
        mp.mandate_processing(self.correct_df)

    def test_mp_raiseError(self):
        """
        Edge test to check whether this function raises an expected error
        """
        try:
            mp.mandate_processing(self.wrong_df)
        except KeyError:
            self.assertRaises(KeyError)


if __name__ == "__main__":
    unittest.main()
