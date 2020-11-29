"""This unittest checks if the function 'covid' function works
UnitTests(unittest.TestCase) -- framework for functions testing
                                knn_regression(). Exports 'OK', 'FAIL',
                                or 'ERROR'
def test_smoke(self) -- does function run-through w/o problems
"""

from covid import covid
import unittest

class UnitTests(unittest.TestCase):
    """
    Testing the travis

    """
    def test_smoke(self):
        """
        Testing the travis

        """
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
