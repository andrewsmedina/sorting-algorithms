from merge_sort import merge_sort

import unittest


class MergeSortTestCase(unittest.TestCase):

    def test_merge_sort_should_sort_a_list(self):
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([4, 2, 3, 5, 1]))


unittest.main()
