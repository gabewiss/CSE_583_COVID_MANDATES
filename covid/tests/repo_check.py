import unittest

import data_retrieval


class TestDataRetrieval(unittest.TestCase):
    """Test the data_retrieval function"""

    def test_edge(self):
        """
        Smoke test on data_retrieval
        """
        try:
            data_retrieval()
        except IOError:
            return print('Website not found')


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataRetrieval)
_ = unittest.TextTestRunner().run(suite)
