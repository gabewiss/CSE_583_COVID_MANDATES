"""This unittest checks if the function 'covid' function works
UnitTests(unittest.TestCase) -- framework for functions testing
                                knn_regression(). Exports 'OK', 'FAIL',
                                or 'ERROR'
def test_smoke(self) -- does function run-through w/o problems
"""

import unittest
from covid import covid


class UnitTests(unittest.TestCase):
    """
    Testing the travis

    """



    def test_smoke(self):
        """
        Testing the travis

        """
        ya = 3

        covid(ya)

        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
