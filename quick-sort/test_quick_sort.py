from quick_sort import quick_sort

import unittest


class QuickSortTestCase(unittest.TestCase):

    def test_quick_sort_should_sort_a_list(self):
        self.assertEqual([1, 2, 3, 4, 5], quick_sort([4, 2, 3, 5, 1]))


unittest.main()
