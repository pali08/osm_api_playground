import unittest

from main import split_into_bins
import numpy.testing as nptest


class MyTestCase(unittest.TestCase):
    def test_split_into_bins(self):
        nptest.assert_almost_equal(split_into_bins(5.5, 6.8, 1), [[5.5, 6.8]])
        nptest.assert_almost_equal(split_into_bins(5.5, 6.8, 2), [[5.5, 6.15], [6.15, 6.8]])
        nptest.assert_almost_equal(split_into_bins(2.5478, 6.8748, 10),
                                   [[2.5478, 2.9805], [2.9805, 3.4132], [3.4132, 3.8459], [3.8459, 4.2786],
                                    [4.2786, 4.7113], [4.7113, 5.144], [5.144, 5.5767], [5.5767, 6.009399999999999],
                                    [6.009399999999999, 6.4421], [6.4421, 6.8748000000000005]])


if __name__ == '__main__':
    unittest.main()
