import unittest

import pandas as pd

from covid import covid


class UnitTests(unittest.TestCase):

    def test_smoke(self):
        """
        Testing the travis

        """
        self.assertTrue(True)
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
