import unittest

import pandas as pd

from CSE_583_COVID_MANDATES import CSE_583_COVID_MANDATES


class UnitTests(unittest.TestCase):

    def test_smoke(self):
        """
        Testing the travis

        """
        self.assertTrue(True)
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
